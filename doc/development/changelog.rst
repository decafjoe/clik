
===========
 Changelog
===========


0.92.3 -- unreleased
====================

* Fixed logic bug that, when an end user is running Python 2.7 and
  does not supply a required positional argument, causes an exception
  within clik instead of printing an error message.


0.92.2 -- 2017-12-19
====================

* Added introductory documentation: example code, tutorial, and
  screencast.


0.92.1 -- 2017-11-28
====================

* Fixed incorrect ``__version__`` attribute.


0.92.0 -- 2017-11-23
====================

* Moved internal ``AttributeDict`` class from ``clik.app`` to
  ``clik.util``.


0.91.0 -- 2017-11-06
====================

* Added a facility for handling unknown arguments.


0.90.2 -- 2017-10-12
====================

* Calling ``run_children()`` when there are no children no longer
  raised an exception; it simply returned 0 (i.e. no error in the
  children).


0.90.1 -- 2017-09-06
====================

* Updated PyPI trove classifier ``Development Status`` from ``1 -
  Planning`` to ``3 - Alpha``.


0.90.0 -- 2017-09-05
====================

* Initial public re-release.


Pre-0.90.0
==========

The Dark Old Days.
