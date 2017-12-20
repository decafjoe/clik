
.. _tutorial-12-exit-code:

========================
 Tutorial 12: Exit Code
========================

There are a lot of places execution can go wrong. clik lets you bail
out at any point by yielding a non-``None`` value. The value yielded
is used as the exit code for the invocation.

…well, kind of. When a subcommand yields non-``None``, clik
immediately starts "unwinding" through the cleanup blocks of the
parent commands. Parent commands can override the exit code from
children.

…and you really can unwind from anywhere. That first yield separating
the "parser config" block from the "do stuff" block? If you yield
non-``None`` from there the application will exit before the parser is
even fully configured. Meaning that it's a *hard* fail, and end users
won't even be able to use ``-h/--help``. In general this isn't what
you want, but consider a situation where a default value to a critical
argument (say, "database host") is expected to be in an environment
variable. You control all the machines the app runs on, and it really
is a situation where, if that variable is not set, all kinds of stuff
is wrong. In that case it might be perfectly appropriate to hard fail
without even initializing the parser. The point is: clik gives you the
choice and makes it easy to do that if you want to.

.. highlight:: python

Back to our application::

  @todo
  def add():
      # ... snip ...
      if item:
          g.item_list.append(item)
          # ... snip ...
      else:
          print('error: empty item', file=sys.stderr)
          yield 1  # <--- !!! new code !!! ---

  # ... snip ...

  @todo
  def done():
      # ... snip ...
      if args.all:
          del g.item_list[:]
      else:
          # ... snip ...
          if -1 < index < len(g.item_list):
              del g.item_list[index]
          else:
              print('error: index out of range:', index, file=sys.stderr)
              yield 1  # <--- !!! new code !!! ---
      # ... snip ...

.. highlight:: none

The application now has an exit code of ``1`` when the user provides
invalid input and, as a nice side effect, the "Updated list" is no
longer printed when the list is not actually updated::

  $ ./todo add ""                                     
  error: empty item

  $ echo $?                                           
  1

  $ ./todo add                                        
  Item to add: 
  error: empty item

  $ echo $?
  1

  $ ./todo add "Pick up nails from the hardware store"

  Updated list:
  0. Pick up nails from the hardware store

  $ echo $?
  0

  $ ./todo done -i asdf
  usage: todo done [-h] [-a | -i INDEX]
  todo done: error: argument -i/--index: invalid int value: 'asdf'

  $ echo $?
  1

  $ ./todo done -i -1
  error: index out of range: -1

  $ echo $?
  1

  $ ./todo done

  0. Pick up nails from the hardware store

  Item number to remove? 5
  error: index out of range: 5

  $ echo $?
  1

  $ ./todo done -i 0

  Updated list:

  $ echo $?
  0

:ref:`One final tweak <tutorial-13-bare>` and the tutorial is
complete!
