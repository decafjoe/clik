
.. _tutorial-11-cleanup:

======================
 Tutorial 11: Cleanup
======================

.. highlight:: python

There's a final phase to execution that we haven't discussed yet:
cleanup. For command functions with subcommands (like our ``todo``
function), cleanup is an optional third block of code that gets run
after child commands have run::

  @app
  def todo():
      # configure argument parser
      yield  # give control back to clik, which parses end user arguments
      # do something with parsed arguments
      yield  # give control back to clik, which runs child commands
      # clean up

This is where we'll persist the changes that subcommands make to
``g.item_list``::

  @app
  def todo():
      # ... snip ...
      yield

      # Same as before
      g.item_list = []
      if os.path.exists(args.file):
          with open(args.file) as f:
              g.item_list = json.load(f)

      # New stuff
      yield

      with open(args.file, 'w') as f:
          json.dump(g.item_list, f, indent=2)
          f.write('\n')

.. highlight:: none

And that's it! The app now does what we sketched out in the first
step::

  $ ls
  bin            lib                       test.json
  include        pip-selfcheck.json        todo

  $ ./todo ls

  $ ls
  bin            pip-selfcheck.json        todo.json
  include        test.json
  lib            todo

  $ cat todo.json
  []

  $ ./todo add "Pick up nails from the hardware store"

  Updated list:
  0. Pick up nails from the hardware store

  $ cat todo.json
  [
    "Pick up nails from the hardware store"
  ]

  $ ./todo ls
  0. Pick up nails from the hardware store

  $ ./todo add
  Item to add: Grab milk from the grocery

  Updated list:
  0. Pick up nails from the hardware store
  1. Grab milk from the grocery

  $ cat todo.json
  [
    "Pick up nails from the hardware store",
    "Grab milk from the grocery"
  ]

  $ ./todo ls
  0. Pick up nails from the hardware store
  1. Grab milk from the grocery

  $ ./todo add "Clean up the kitchen"

  Updated list:
  0. Pick up nails from the hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen

  $ ./todo add "Feed the cats"

  Updated list:
  0. Pick up nails from the hardware store
  1. Grab milk from the grocery
  2. Clean up the kitchen
  3. Feed the cats

  $ cat todo.json  
  [
    "Pick up nails from the hardware store",
    "Grab milk from the grocery",
    "Clean up the kitchen",
    "Feed the cats"
  ]

  $ ./todo done -i 2

  Updated list:
  0. Pick up nails from the hardware store
  1. Grab milk from the grocery
  2. Feed the cats

  $ cat todo.json
  [
    "Pick up nails from the hardware store",
    "Grab milk from the grocery",
    "Feed the cats"
  ]

  $ ./todo done

  0. Pick up nails from the hardware store
  1. Grab milk from the grocery
  2. Feed the cats

  Item number to remove? 1

  Updated list:
  0. Pick up nails from the hardware store
  1. Feed the cats

  $ cat todo.json
  [
    "Pick up nails from the hardware store",
    "Feed the cats"
  ]

  $ ./todo done -a

  Updated list:

  $ cat todo.json
  []

It works. Cool.

In the next couple steps we'll put on some finishing touches by
:ref:`implementing error codes <tutorial-12-exit-code>` for our couple
user-input-error situations, then adding one final tweak to let users
simply run ``./todo`` to get a list of items (instead of ``./todo
list``).
