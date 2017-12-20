
.. _tutorial-02-main:

===================
 Tutorial 02: Main
===================

.. highlight:: python

The next step is to structure our file the "standard" way for Python
files that are used as executables. Note that the ``import clik``
statement is gone; now that we've tested that we can import it, we
don't need it for the moment. We'll bring it back in a couple steps.

::

  #!bin/python

  if __name__ == '__main__':
      print('Hello, world!')

``__name__`` is a special variable that contains the name of the
current module as a string. This is useful because Python lets a file
be both "``import`` -able" and executable. If we were to import the
``todo.py`` file from another module, ``__name__`` would be equal to
``"todo"``.

.. highlight:: sh

When run directly, however, ``__name__`` is set to the special value
``"__main__"``. By checking for that special value and running our
code only when it's set, it allows our file to "do the right thing"
whether it's imported or run directly::

  $ ./todo.py
  Hello, world!
  $ python
  # ... snip ...
  >>> import todo
  >>> # note that "hello world" is not printed above
  >>> exit()
  $

For the demo application, this doesn't matter very much – it is meant
to always be run directly. And in fact, in the next step we'll make a
change that makes it unimportable. Using this pattern is still good
form, however, since it's an obvious marker for how the file is
intended to be used (i.e. as an executable).

In the next step, we'll :ref:`remove the .py extension
<tutorial-03-filename>` to make the app more caller-friendly, then
we'll finally be ready to get into clik proper!
