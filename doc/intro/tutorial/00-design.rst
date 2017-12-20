
.. _tutorial-00-design:

=====================
 Tutorial 00: Design
=====================

Before writing any code, let's make a rough sketch of what the
application should do.

In prose: ``todo`` should allow the end user to manage a todo list.
Items may be added and deleted, and the current list may be displayed.

We'll keep data storage simple. The underlying data structure will be
a list of strings. We'll use Python's built-in JSON module to persist
the data to a file.

.. highlight:: sh

Roughing out the interface::

  todo [-f/--file=todo.json] <COMMAND AND ARGS ...>
  todo add ["item to add"]        # prompt if item not given
  todo list                       # print a 0-indexed list of items
  todo done [-i/--index|-a/--all] # if -a/--all given, all items are done
                                  # else if 0-based index supplied,
                                  #   delete item at that index
                                  # else print list and prompt for index

The final implementation may not look exactly like this, but it's a
good place to start!

Next, let's :ref:`set up the environment <tutorial-01-setup>` for the
app.
