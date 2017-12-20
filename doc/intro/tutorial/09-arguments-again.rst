
.. _tutorial-09-arguments-again:

===============================
 Tutorial 09: Arguments, Again
===============================

.. highlight:: python

Adding arguments to the subcommands should look familiar::

  @todo
  def add():
      """Add an item to the list."""
      parser.add_argument(
          'item',
          default=None,
          help='item to add (prompts if not supplied)',
          nargs='?',
      )
      yield
      print('item:', args.item)

  # ... snip ...

  @todo
  def done():
      """
      Remove an item from the list.
  
      If no arguments are supplied, the current list is printed and
      the program prompts for the index of the item to remove.
      """
      group = parser.add_mutually_exclusive_group()
      group.add_argument(
          '-a',
          '--all',
          action='store_true',
          default=False,
          help='remove all items from the list',
      )
      group.add_argument(
          '-i',
          '--index',
          default=None,
          help='0-based index of the item to remove',
          type=int,
      )
      yield
      print('index:', args.index)
      print('all:', args.all)

We use the same ``parser`` and ``args`` variables to configure and
access arguments in subcommands! This is part of the "magic" provided
by clik. When used in the ``todo`` function, ``parser`` refers to the
top-level parser for the app. When used in a subcommand, ``parser``
refers to the subparser for that subcommand.

.. note::

   This type of magic will turn off some Pythonistas; it's totally
   cool if you feel a little dirty and maybe a little angry right now.
   I mean, I wrote the thing and I'm still not totally sure how to
   feel about this part of it. All I can say is: I've been using this
   pattern for a few years now as clik has taken this final shape and,
   except for the occasional ringing of "explicit is better than
   implicit" in my head, it's been quite pleasant.

.. highlight:: none

The ``todo`` app now has the UI we sketched out at the very
beginning::

  $ ./todo add -h            
  usage: todo add [-h] [item]

  Add an item to the list.

  positional arguments:
    item        item to add (prompts if not supplied)

  optional arguments:
    -h, --help  show this help message and exit

  $ ./todo add
  item: None

  $ ./todo add "Wash the car"
  item: Wash the car

  $ ./todo done -h
  usage: todo done [-h] [-a | -i INDEX]

  Remove an item from the list.

  optional arguments:
    -h, --help            show this help message and exit
    -a, --all             remove all items from the list
    -i INDEX, --index INDEX
                          0-based index of the item to remove

  If no arguments are supplied, the current list is printed and the program
  prompts for the index of the item to remove.

  $ ./todo done
  index: None
  all: False

  $ ./todo done -i 2
  index: 2
  all: False

  $ ./todo done -a  
  index: None
  all: True

  $ ./todo done -a -i 2
  usage: todo done [-h] [-a | -i INDEX]
  todo done: error: argument -i/--index: not allowed with argument -a/--all

.. highlight:: python

To show that ``parser`` is, in fact, different for the different
subcommands, let's try to use an argument in ``done`` that is defined
in ``add``::

  @todo
  def done():
      # ... snip ...
      yield
      print('item:', args.item)  # defined in add

.. highlight:: none

In the shell::

  $ ./todo done
  Traceback (most recent call last):
    File "./todo", line 83, in <module>
      todo.main()

  # ... snip traceback ...

  AttributeError: 'Namespace' object has no attribute 'item'

So that's most of what makes clik clik: ``parser``, ``args``, and
subcommands.

We're now in the home stretch! Just a couple more steps and the
application will be ready to ship.

(Also, I'd like to take this chance to thank you for continuing to
read. I didn't know whether you'd be angry about that magic globals
thing, and honestly I was a little afraid to bring it up with you. But
now that we have that behind us and we're all cool, let's finish up
this app shall we?)

Let's circle back and :ref:`make the list command print the items
<tutorial-10-global>` loaded from the data file.
