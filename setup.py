# -*- coding: utf-8 -*-
"""
Package configuration for clik.

:author: Joe Joyce <joe@decafjoe.com>
:copyright: Copyright (c) Joe Joyce, 2009-2017.
:license: BSD
"""
import os

from setuptools import find_packages, setup


name = 'clik'
version = '0.9.0'
requires = ()

root = os.path.abspath(os.path.dirname(__file__))


def read(filename, default):
    """
    Read and return content of FILENAME (or FILENAME.rst) from root directory.

    If neither of the files exist, ``default`` is returned.
    """
    path = os.path.join(root, filename)
    if os.path.exists(path):
        return open(path).read()
    path = '%s.rst' % path
    if os.path.exists(path):
        return open(path).read()
    return default


changelog = read('CHANGELOG', 'No changelog present.')
readme = read('README', 'No readme present.')
long_description = '%s\n\n%s' % (readme, changelog)

setup(
    author='Joe Joyce',
    author_email='joe@decafjoe.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    description='Library for writing subcommand-style command-line apps.',
    install_requires=requires,
    license='BSD',
    long_description=long_description,
    name=name,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    url='https://bitbucket.org/decafjoe/%s' % name,
    version=version,
    zip_safe=False,
)
