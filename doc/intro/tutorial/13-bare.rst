
.. _tutorial-13-bare:

===================
 Tutorial 13: Bare
===================

It turns out the grumpy systems administrators from
:ref:`tutorial-08-aliases` were right. Printing the todo list is such
a common operation that the extra characters (even with the shortened
``ls`` alias) are having company-wide impacts on todo-related
productivity.

It would make a lot of sense if running ``./todo`` without any
arguments just printed the todo list.

Using clik, it can! "Bare commands" (named as such because I spent two
weeks thinking about it and couldn't come up with anything better)
allow a command with subcommands – which would normally require one of
the subcommands to be supplied – to be invoked "bare" (i.e. without a
subcommand).

There are some (serious) limitations:

* Positional arguments are not allowed for bare commands (if the user
  runs ``./app foo`` is ``foo`` a subcommand or a positional
  argument?)
* Mutually exclusive groups are not allowed (this is an internal
  limitation)
* Unknown arguments are not allowed (similar rationale to positional
  arguments) *(note: unknown arguments are not covered in the
  tutorial)*

So it's far from perfect, but it's better than nothing.

.. highlight:: python

Implementing the "bare" command for our ``todo`` app::

  @todo.bare
  def bare():
      yield
      print_list()

.. highlight:: none

Poking around in the shell (note the updated usage statement)::

  $ ./todo -h
  usage: todo [-h] [-f FILE] {add,list,done} ...
         todo [-h] [-f FILE]

  Command-line application for managing a todo list.

  optional arguments:
    -h, --help            show this help message and exit
    -f FILE, --file FILE  file in which to store data (default: todo.json)

  subcommands:
    {add,list,done}
      add                 Add an item to the list.
      list (ls)           Show the items on the list.
      done                Remove an item from the list.

  The list is stored on disk as a simple JSON file containing an array of
  strings. The file path is controlled by the -f/--file argument (see
  documentation for that argument for more information).

  $ ./todo add "Pick up nails from the hardware store"
  # ... snip ...

  $ ./todo
  0. Pick up nails from the hardware store

  $ ./todo add "Grab milk from the grocery"           
  # ... snip ...

  $ ./todo                                 
  0. Pick up nails from the hardware store
  1. Grab milk from the grocery

  $ ./todo ls
  0. Pick up nails from the hardware store
  1. Grab milk from the grocery

And so, the demo application is finally complete. Ship it!
