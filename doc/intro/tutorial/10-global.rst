
.. _tutorial-10-global:

=====================
 Tutorial 10: Global
=====================

.. highlight:: python

Right now, the todo items are "locked up" inside the ``todo``
function::

  @app
  def todo():
      # ... snip ...
      yield

      item_list = []
      if os.path.exists(args.file):
          with open(args.file) as f:
              item_list = json.load(f)

``add``, ``list``, and ``done`` all need to access/modify
``item_list``. How?

This is a common need for applications. The top-level app object
reads data/configuration/etc, or opens a database connection, or
sets up a client for a remote service – or whatever – and the
subcommands use those "handles" to do their work.

clik provides a "global" object, ``g``, to facilitate passing around
global data/connection handles/etc::

  from clik import app, args, g, parser  # note the g

  @app
  def todo():
      # ... snip ...
      yield

      g.item_list = []
      if os.path.exists(args.file):
          with open(args.file) as f:
              g.item_list = json.load(f)

  # ... snip ...

  @todo(name='list', alias='ls')
  def list_():
      """Show the items on the list."""
      yield
      for i, item in enumerate(g.item_list):
          print('%i. %s' % (i, item))

.. highlight:: json

Assuming the ``test.json`` file from before (with the following
contents)…

::

  [
    "Pick up nails from hardware store",
    "Grab milk from the grocery",
    "Clean up the kitchen",
    "Feed the cats"
  ]

.. highlight:: none

… ``list`` now prints our 0-indexed list of items::

  $ ./todo -f test.json list 
  0. Pick up nails from hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen
  3. Feed the cats

.. highlight:: python

Under the covers, ``g`` is just a dictionary that allows you to access
values using attributes instead of brackets. The following sets of
operations are identical::

  g.foo = 'bar'
  g['foo'] = 'bar'

  g.foo
  g['foo']

  del g.foo
  del g['foo']

We already know we'll need to print the 0-indexed list output inside
``done``, so let's factor it out into a function::

  def print_list():
      for i, item in enumerate(g.item_list):
          print('%i. %s' % (i, item))

  # ... snip ...

  @todo(name='list', alias='ls')
  def list_():
      """Show the items on the list."""
      yield
      print_list()
  
Since we're thinking about it, let's go ahead and implement ``done``::

  import sys

  # ... snip ...

  @todo
  def done():
      # ... snip ...
      yield

      if args.all:
          del g.item_list[:]
      else:
          index = args.index
          while index is None:
              print()
              print_list()
              print()
              selection = input('Item number to remove? ')
              try:
                  index = int(selection)
              except ValueError:
                  print('error: not an integer:', selection, file=sys.stderr)
          if -1 < index < len(g.item_list):
              del g.item_list[index]
          else:
              print('error: index out of range:', index, file=sys.stderr)

      print()
      print('Updated list:')
      print_list()

This is all straightforward Python code; going over the details of the
implementation is beyond the scope of this tutorial.

``add`` is simpler and shorter than ``done``::

  @todo
  def add():
      # ... snip ...
      yield
      item = args.item
      if item is None:
          item = input('Item to add: ') or None
      if item:
          g.item_list.append(item)
          print()
          print('Updated list:')
          print_list()
      else:
          print('error: empty item', file=sys.stderr)

.. highlight:: none

Playing with the new commands and the ``test.json`` file, we see that
things are generally working. Changes are not persisted to disk, but
we'll tackle that problem in the next step.

::

  $ ./todo -f test.json ls                            
  0. Pick up nails from hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen
  3. Feed the cats

  $ ./todo -f test.json add "Hang picture on the wall"

  Updated list:
  0. Pick up nails from hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen
  3. Feed the cats
  4. Hang picture on the wall

  $ ./todo -f test.json add                           
  Item to add: Hang picture on the wall

  Updated list:
  0. Pick up nails from hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen
  3. Feed the cats
  4. Hang picture on the wall

  $ ./todo -f test.json add ""
  error: empty item

  $ ./todo -f test.json add ""                        
  Item to add:
  error: empty item

  $ ./todo -f test.json ls 
  0. Pick up nails from hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen
  3. Feed the cats

  $ ./todo -f test.json done -i 2

  Updated list:
  0. Pick up nails from hardware store
  1. Grab milk from the grocery
  2. Feed the cats

  $ ./todo -f test.json done -a  

  Updated list:

  $ ./todo -f test.json done   

  0. Pick up nails from hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen
  3. Feed the cats

  Item number to remove? 3

  Updated list:
  0. Pick up nails from hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen

  $ ./todo -f test.json done -i 10
  error: index out of range: 10

  Updated list:
  0. Pick up nails from hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen
  3. Feed the cats

  $ ./todo -f test.json done      

  0. Pick up nails from hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen
  3. Feed the cats

  Item number to remove? foo
  error: not an integer: foo

  0. Pick up nails from hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen
  3. Feed the cats

  Item number to remove? 12
  error: index out of range: 12

  Updated list:
  0. Pick up nails from hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen
  3. Feed the cats

Nice! The application has really started to take shape. Next we'll
save the changes to disk using :ref:`cleanup code in the app function
<tutorial-11-cleanup>`.

.. note::

   ``g`` (along with the magic ``parser`` and ``args`` variables) is
   the other design decision experienced Pythonistas might
   (rightfully) sneer at. Global variables are generally discouraged
   in Python, and ``g`` actively encourages their use (even if veiled
   behind a not-technically-a-global-depending-on-how-you-look-at-it
   proxy object).

   The justification is the same as for ``parser`` / ``args``. This
   "``g`` pattern" is one I've used extensively (in clik and in Flask)
   and, while it may be against the Zen of Python, it's damn useful.
   *Used judiciously*, it can be a real boon to productivity and
   overall code clarity.
