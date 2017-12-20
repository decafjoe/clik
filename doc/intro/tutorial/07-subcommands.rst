
.. _tutorial-07-subcommands:

==========================
 Tutorial 07: Subcommands
==========================

.. note::

   This step is a bit longer and more involved than the others because
   it tries to tie together the core concepts in clik, and emphasize
   the pattern that underlies the library.

   The important code updates are all in the first listing. The rest
   of the step explains what's going on using silly, verbose examples
   for the sake of illustration.

.. highlight:: python

To this point, everything we have done would be just as easy using
stock argparse. clik really starts to shine when we introduce
subcommands::

  @app
  def todo():
      # ... snip ...

      # The following lines have been deleted from the example.
      # for item in item_list:
      #     print('*', item)

  @todo
  def add():
      """Add an item to the list."""
      yield
      print('hello from add')

  @todo(name='list')
  def list_():
      """Show the items on the list."""
      yield
      print('hello from list')

  @todo
  def done():
      """Remove an item from the list."""
      yield
      print('hello from done')


.. highlight:: none

Poking around at the application::

  $ ./todo -h           
  usage: todo [-h] [-f FILE] {add,list,done} ...

  Command-line application for managing a todo list.

  optional arguments:
    -h, --help            show this help message and exit
    -f FILE, --file FILE  file in which to store data (default: todo.json)

  subcommands:
    {add,list,done}
      add                 Add an item to the list.
      list                Show the items on the list.
      done                Remove an item from the list.

  The list is stored on disk as a simple JSON file containing an array of
  strings. The file path is controlled by the -f/--file argument (see
  documentation for that argument for more information).

  $ ./todo       
  usage: todo [-h] [-f FILE] {add,list,done} ...
  todo: error: the following arguments are required: {add,list,done}

  $ ./todo add -h
  usage: todo add [-h]

  Add an item to the list.

  optional arguments:
    -h, --help  show this help message and exit

  $ ./todo add   
  hello from add

  $ ./todo list -h
  usage: todo list [-h]

  Show the items on the list.

  optional arguments:
    -h, --help  show this help message and exit

  $ ./todo list
  hello from list

  $ ./todo done -h
  usage: todo done [-h]

  Remove an item from the list.

  optional arguments:
    -h, --help  show this help message and exit

  $ ./todo done
  hello from done

Neat-o! Gluing all that together with argparse would have been
straightforward, but would have involved quite a bit of ceremony and
boilerplate.

Subcommands look a lot like the ``app`` we've been working on to this
point. (There is a reason for this – under the covers they're actually
the same thing. :class:`clik.app.App` is a subclass of
:class:`clik.command.Command`!)

.. highlight:: python

The function decorated by ``app`` (``todo`` in our case) can itself be
used as a decorator to register a subcommand::

  @todo
  def xyz():
      # ... do subcommand stuff ...

.. note::

   Once a single subcommand has been registered, it is no longer valid
   for end users to invoke the application without a subcommand.
   (Unless a "bare" subcommand has been registered – more on that
   later.)

Subcommands can also be used as decorators to register
sub-subcommands. It's "turtles all the way down." An example, with a
slew of dummy sub- (and sub-sub- and sub-sub-sub-) commands::

  @todo
  def foo():
      yield

  @foo
  def spam():
      yield
      print('hai from foo spam')

  @foo
  def ham():
      yield
      print('hai from foo ham')

  @foo
  def eggs():
      yield

  @eggs
  def alpha():
      yield
      print('hai from foo eggs alpha')

  @eggs
  def bravo():
      yield
      print('hai from foo eggs bravo')

  @eggs
  def charlie():
      yield
      print('hai from foo eggs charlie')


.. highlight:: none

Poking around in the shell::

  $ ./todo foo -h     
  usage: todo foo [-h] {spam,ham,eggs} ...

  optional arguments:
    -h, --help       show this help message and exit

  subcommands:
    {spam,ham,eggs}
      spam
      ham
      eggs

  $ ./todo foo        
  usage: todo foo [-h] {spam,ham,eggs} ...
  todo foo: error: the following arguments are required: {spam,ham,eggs}

  $ ./todo foo spam
  hai from foo spam

  $ ./todo foo ham 
  hai from foo ham

  $ ./todo foo eggs
  usage: todo foo eggs [-h] {alpha,bravo,charlie} ...
  todo foo eggs: error: the following arguments are required: {alpha,bravo,charlie}

  $ ./todo foo eggs -h
  usage: todo foo eggs [-h] {alpha,bravo,charlie} ...

  optional arguments:
    -h, --help            show this help message and exit

  subcommands:
    {alpha,bravo,charlie}
      alpha
      bravo
      charlie

  $ ./todo foo eggs alpha -h
  usage: todo foo eggs alpha [-h]

  optional arguments:
    -h, --help  show this help message and exit

  $ ./todo foo eggs alpha   
  hai from foo eggs alpha

  $ ./todo foo eggs bravo
  hai from foo eggs bravo

  $ ./todo foo eggs charlie
  hai from foo eggs charlie

Like the ``app``, the name for the subcommand defaults to the name of
the function being decorated and can be overridden by passing the
``name`` parameter to the decorator.

.. highlight:: python

This is useful for our ``list`` command since it's a bad idea to
redefine built-in functions (which ``list`` is). We use ``list_`` as
the function name, and pass ``"list"`` to clik as the name *it* should
use::

  @todo(name='list')
  def list_():
      """Show the items on the list."""
      yield
      print('hello from list')

.. highlight:: none

The app, of course, works the same as it did before::

  $ ./todo -h           
  usage: todo [-h] [-f FILE] {add,list,done} ...

  Command-line application for managing a todo list.

  optional arguments:
    -h, --help            show this help message and exit
    -f FILE, --file FILE  file in which to store data (default: todo.json)

  subcommands:
    {add,list,done}
      add                 Add an item to the list.
      list                Show the items on the list.
      done                Remove an item from the list.

  The list is stored on disk as a simple JSON file containing an array of
  strings. The file path is controlled by the -f/--file argument (see
  documentation for that argument for more information).

  $ ./todo list -h
  usage: todo list [-h]

  Show the items on the list.

  optional arguments:
    -h, --help  show this help message and exit

  $ ./todo list
  hello from list

.. highlight:: python

As you've probably noticed, help messages are taken from docstrings.
Like the ``app``, content before the blank line is the ``description``
and everything after is the ``epilog``. As an example, let's "lorem
ipsum" the help for ``add``::

  @todo
  def add():
      """
      Add an item to the list.

      Lorem ipsum dolor sit amet, consectetur adipiscing elit. In
      congue porttitor ornare. Aenean ac diam ipsum. Sed sit amet
      libero ut ligula pretium consectetur eu quis justo. Integer
      sollicitudin velit et nunc suscipit laoreet.
      """
      yield
      print('hello from add')

.. highlight:: none

Predictably, the help text is::

  $ ./todo -h              
  usage: todo [-h] [-f FILE] {add,list,done} ...

  Command-line application for managing a todo list.

  optional arguments:
    -h, --help            show this help message and exit
    -f FILE, --file FILE  file in which to store data (default: todo.json)

  subcommands:
    {add,list,done}
      add                 Add an item to the list.
      list                Show the items on the list.
      done                Remove an item from the list.

  The list is stored on disk as a simple JSON file containing an array of
  strings. The file path is controlled by the -f/--file argument (see
  documentation for that argument for more information).

  $ ./todo add -h
  usage: todo add [-h]

  Add an item to the list.

  optional arguments:
    -h, --help  show this help message and exit

  Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue porttitor
  ornare. Aenean ac diam ipsum. Sed sit amet libero ut ligula pretium
  consectetur eu quis justo. Integer sollicitudin velit et nunc suscipit
  laoreet.

Nice! We are moving right along. Next we'll take :ref:`a quick look at
aliases <tutorial-08-aliases>` before circling back to arguments for
our subcommands.
