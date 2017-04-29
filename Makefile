#
# Makefile for the clik project.
#
# Copyright Joe Joyce, 2009-2017. All rights reserved.
#

PROJECT = clik

# Virtualenv command
VIRTUALENV ?= virtualenv

# "Main" python version for development
PYTHON_VERSION = python3.6

# Base directories
ROOT := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
ENV = $(ROOT)/.env
DOC = $(ROOT)/doc
SRC = $(ROOT)/src
TOOL = $(ROOT)/tool

# Code
SETUP = $(ROOT)/setup.py
REQUIREMENTS = $(ROOT)/requirements.txt
ENV_SOURCES = $(SETUP) $(REQUIREMENTS)
CHANGELOG = $(ROOT)/CHANGELOG.rst
README = $(ROOT)/README.rst
SOURCES := $(shell find $(SRC) -name "*.py")
UPDATED_ENV = $(ENV)/updated

# Commands
COVERAGE = $(ENV)/bin/coverage
CRAM = $(ENV)/bin/cram
FLAKE8 = $(ENV)/bin/flake8
PIP = $(ENV)/bin/pip
PYTHON = $(ENV)/bin/python
SPHINX = $(ENV)/bin/sphinx-build
TOX = $(ENV)/bin/tox
TWINE = $(ENV)/bin/twine

# Distribution
VERSION = $(shell python $(ROOT)/setup.py --version)
DIST = $(ROOT)/dist/$(PROJECT)-$(VERSION).tar.gz

# Python package settings
FORCE_UPDATES_TO_PYTHON_PACKAGES = pip setuptools wheel
IGNORE_UPDATES_TO_PYTHON_PACKAGES = "\($(PROJECT)\)\|\(virtualenv\)"

# Git hooks
PRE_COMMIT = $(ROOT)/.git/hooks/pre-commit
# TODO: Figure out what this should be (make lint?)
PRE_COMMIT_HOOK = true
PRE_PUSH = $(ROOT)/.git/hooks/pre-push
# TODO: Figure out what this should be (make test?)
PRE_PUSH_HOOK = true


help :
	@printf "usage: make <target> where target is one of:\n\n"
	@printf "  check-update  Check for updates to dependencies\n"
	@printf "  clean         Delete build artifacts (dists, .pyc, etc)\n"
	@printf "  docs          Generate PDF and HTML documentation\n"
	@printf "  dist          Create sdist in dist/\n"
	@printf "  env           Install development environment\n"
	@printf "  html          Generate HTML documentation\n"
	@printf "  lint          Run linter on code\n"
	@printf "  pdf           Generate PDF documentation\n"
	@printf "  pristine      Delete development environment\n"
	@printf "  release       Cut a release of the software\n"
	@printf "  test          Run all tests\n"
	@printf "  test-cover    Run tests, report test coverage\n"
	@printf "  test-tox      Run tests, all supported Python versions\n\n"


# =============================================================================
# ----- Environment -----------------------------------------------------------
# =============================================================================

$(PYTHON) :
	$(VIRTUALENV) --python=$(PYTHON_VERSION) $(ENV)

$(PIP) : $(PYTHON)

$(UPDATED_ENV) : $(PIP) $(ENV_SOURCES)
	$(PIP) install -U $(FORCE_UPDATES_TO_PYTHON_PACKAGES)
	$(PIP) install \
		--editable $(ROOT) \
		--requirement $(REQUIREMENTS)
	touch $(UPDATED_ENV)

env : $(PRE_COMMIT) $(PRE_PUSH) $(UPDATED_ENV)

check-update : env
	@printf "Checking for library updates...\n"
	@$(PIP) list --outdated --local --format=columns | \
		grep -v $(IGNORE_UPDATES_TO_PYTHON_PACKAGES) ||\
		printf "All libraries are up to date :)\n"

pristine : clean
	git -C $(ROOT) clean -dfX
	rm $(PRE_COMMIT) $(PRE_PUSH)


# =============================================================================
# ----- QA/Test ---------------------------------------------------------------
# =============================================================================

$(PRE_COMMIT) : $(ROOT)/Makefile
	echo "$(PRE_COMMIT_HOOK)" > $(PRE_COMMIT)
	chmod +x $(PRE_COMMIT)

$(PRE_PUSH) : $(ROOT)/Makefile
	echo "$(PRE_PUSH_HOOK)" > $(PRE_PUSH)
	chmod +x $(PRE_PUSH)

lint : env
	$(FLAKE8) --ignore=D203 $(DOC)/conf.py $(SETUP) $(SOURCES)
	@printf "Flake8 is happy :)\n"

test-cover : env
	cd $(ROOT); \
		$(COVERAGE) run setup.py test; \
		$(COVERAGE) report; \
		$(COVERAGE) html

test-tox : env
	cd $(ROOT); $(TOX)

test : lint test-tox test-cover


# =============================================================================
# ----- Documentation ---------------------------------------------------------
# =============================================================================

html : env
	make -C $(DOC) html SPHINXBUILD=$(SPHINX)

pdf : env
	make -C $(DOC) latexpdf SPHINXBUILD=$(SPHINX)

docs: html pdf


# =============================================================================
# ----- Build -----------------------------------------------------------------
# =============================================================================

$(DIST) : $(README) $(SOURCES) $(UPDATED_ENV)
	mv $(CHANGELOG) CHANGELOG; mv $(README) README
	-cd $(ROOT) && $(PYTHON) setup.py sdist && touch $(DIST)
	mv CHANGELOG $(CHANGELOG); mv README $(README)

dist : $(DIST)

release :
	$(TOOL)/pre-release
	cd $(ROOT); make lint test-tox clean dist
	$(TWINE) upload $(DIST)
	$(TOOL)/post-release $(VERSION)

clean :
	cd $(ROOT) && rm -rf \
		$(shell find $(ROOT) -type f -name .DS_Store) \
		$(shell find $(SRC) -type f -name *.pyc) \
		.coverage \
		coverage \
		dist