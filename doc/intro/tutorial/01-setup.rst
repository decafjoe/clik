
.. _tutorial-01-setup:

====================
 Tutorial 01: Setup
====================

For the purposes of the tutorial, we'll create a new virtual
environment, install the ``clik`` package, and put the application
code inside the environment's directory. For the hashbang line of the
app, we'll "cheat" and use a relative path to the virtualenv's Python
interpreter (so it has access to ``clik``). If you were developing a
"real" end-user application, you would probably want to use a
proper package structure.

This means the demo app always has to be called from the working
directory that contains it (i.e. ``./todo.py <...>``). If you really
need to run this from other working directories, change the
``bin/python`` in the first line of the file to an absolute path to
the environment's Python interpreter.

.. highlight:: sh

The following commands create the basic structure::

   $ virtualenv todo
   # ... snip ...
   $ cd todo
   $ bin/pip install clik
   # ... snip ...
   $ touch todo.py
   $ chmod +x todo.py

.. highlight:: python

Open the ``todo.py`` file and edit it to contain::

   #!bin/python
   import clik
   print('Hello, world!')

.. highlight:: sh

Now you should be able to run the script::

  $ ./todo.py
  Hello, world!
  $

If there are no errors, cool! Everything is working. In the next step
we'll tweak the file to :ref:`use the if-name-main pattern
<tutorial-02-main>` common for Python executables.
