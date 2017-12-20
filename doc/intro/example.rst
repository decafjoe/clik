
=========
 Example
=========

.. highlight:: python

Following is the full code listing from the final step of the
tutorial. See :ref:`the design sketch <tutorial-00-design>` for what
this code is meant to accomplish.

::

  #!bin/python
  # -*- coding: utf-8; mode: python -*-
  import json
  import os
  import sys

  from clik import app, args, g, parser


  def print_list():
      for i, item in enumerate(g.item_list):
          print('%i. %s' % (i, item))


  @app
  def todo():
      """
      Simple application for managing a todo list.
  
      The data is stored as a JSON file, which defaults to todo.json.
      See above for more information about arguments and subcommands.
      """
      parser.add_argument(
          '-f',
          '--file',
          default='todo.json',
          help='file in which to store data (default: %(default)s)',
      )

      yield

      g.item_list = []
      if os.path.exists(args.file):
          with open(args.file) as f:
              g.item_list = json.load(f)

      yield

      with open(args.file, 'w') as f:
          json.dump(g.item_list, f, indent=2)
          f.write('\n')


  @todo.bare
  def bare():
      yield
      print_list()


  @todo
  def add():
      """Add an item to the todo list."""
      parser.add_argument(
          'item',
          help='item to add to do the todo list',
          nargs='?',
      )

      yield

      item = args.item
      if item is None:
          item = input('Item to add: ')
      if item:
          g.item_list.append(item)
      else:
          print('error: empty item', file=sys.stderr)
          yield 1

      print()
      print('Updated list:')
      print_list()


  @todo(name='list', alias='ls')
  def list_():
      """Show the items on the todo list."""
      yield
      print_list()


  @todo
  def done():
      """Remove an item from the todo list."""
      group = parser.add_mutually_exclusive_group()
      group.add_argument(
          '-a',
          '--all',
          action='store_true',
          default=False,
          help='mark all items as complete',
      )
      group.add_argument(
          '-i',
          '--index',
          help='integer index of the item to mark as complete',
          type=int,
      )

      yield

      if args.all:
          del g.item_list[:]
      else:
          index = args.index
          while index is None:
              print()
              print_list()
              print()
              selection = input('Index of item to delete? ')
              try:
                  index = int(selection)
              except ValueError:
                  print('error: invalid int value:', selection, file=sys.stderr)
          if -1 < index < len(g.item_list):
              del g.item_list[index]
          else:
              print('error: index out of bounds:', index, file=sys.stderr)
              yield 1

      print()
      print('Updated list:')
      print_list()


  if __name__ == '__main__':
      todo.main()
