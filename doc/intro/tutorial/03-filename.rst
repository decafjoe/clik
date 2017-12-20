
.. _tutorial-03-filename:

=======================
 Tutorial 03: Filename
=======================

Personally I don't like the ``.py`` extension for CLI apps. And clik
doesn't care. So the demo app will be renamed to just ``todo``.

.. highlight:: python
  
Since the filename no longer has an extension, we'll add a modeline to
keep it editor-friendly. We'll add the encoding specifier as well,
since that is good practice in general::

  #!bin/python
  # -*- coding: utf-8; mode: python -*-

  if __name__ == '__main__':
      print('Hello, world!')

.. highlight:: sh

Renaming and running the app should produce the same results as
before::

  $ mv todo.py todo
  $ ./todo
  Hello, world!
  $

Excellent. Now we can :ref:`start getting into clik proper
<tutorial-04-app>`.
