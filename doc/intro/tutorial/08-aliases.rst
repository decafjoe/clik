
.. _tutorial-08-aliases:

======================
 Tutorial 08: Aliases
======================

For discoverability, it's always a good idea to give your commands
descriptive names. For commands that are commonly used, though, this
can be a burden on end users. clik allows you to define aliases for
these commands, giving your application the best of both worlds:
discoverability for new users and concision for power users.

Let's say the end users of our todo program are grumpy systems
administrators that are used to typing ``ls`` instead of ``list``. The
extra ``i`` and ``t`` are causing a serious problem for todo-related
productivity.

.. highlight:: python

An alias makes everyone happy::

  @todo(name='list', alias='ls')
  def list_():
      """Show the items on the list."""
      yield
      print('hello from list')

.. highlight:: none

In the shell::

  $ ./todo -h    
  usage: todo [-h] [-f FILE] {add,list,done} ...

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

  $ ./todo list -h
  usage: todo list [-h]

  Show the items on the list.

  optional arguments:
    -h, --help  show this help message and exit

  $ ./todo ls -h
  usage: todo list [-h]

  Show the items on the list.

  optional arguments:
    -h, --help  show this help message and exit

  $ ./todo list
  hello from list

  $ ./todo ls
  hello from list

.. highlight:: python

If a command has multiple aliases, supply the ``aliases`` argument
instead. For example, if we wanted ``list`` to be aliased to ``ls``
and ``l``::

  @todo(name='list', aliases=('ls', 'l'))
  def list_():
      """Show the items on the list."""
      yield
      print('hello from list')

Note: it's perfectly valid to supply both ``alias`` and ``aliases``.
The reason there are two separate parameters is simply to make calling
code read more naturally.

Next, we'll :ref:`add arguments to the subcommands
<tutorial-09-arguments-again>` and finally have a UI that looks like
the one we sketched out in step 0!
