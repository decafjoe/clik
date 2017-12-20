
.. _tutorial-04-app:

==================
 Tutorial 04: App
==================

.. note::

   This step is a bit longer and more involved than the others because
   it goes over some fundamentals that make subsequent steps smaller
   and easier to explain.

.. highlight:: python

With all the "formalities" out of the way, we can turn the Python
script into a clik app::

  #!bin/python
  # -*- coding: utf-8; mode: python -*-
  from clik import app

  @app
  def todo():
      yield
      print('Hello, world!')

  if __name__ == '__main__':
      todo.main()

.. highlight:: none

Running the program with no arguments produces the same results as
before. If we run it with ``-h`` or ``--help``, though, the app now
has a help message! And if we run it with any other arguments, we get
an error message indicating that our program is not expecting them::

  $ ./todo
  Hello, world!

  $ ./todo -h
  usage: todo [-h]

  optional arguments:
    -h, --help  show this help message and exit

  $ ./todo --help
  usage: todo [-h]

  optional arguments:
    -h, --help  show this help message and exit

  $ ./todo --foo
  usage: todo [-h]
  todo: error: unrecognized arguments: --foo

  $ echo $?
  1

.. highlight:: python

Looking at the new code chunk by chunk::

  from clik import app

First the ``app`` decorator is imported. All the clik interfaces you
will interact with will be imported from the top-level ``clik``
package.

The ``app`` decorator tells clik what to call when your application is
invoked. Here, we tell clik to call ``todo`` when the end user runs
the application::

  @app
  def todo():
      # ... snip ...

The ``app`` decorator also controls the name of the application as
seen in the usage and other automatically generated help messages. By
default, ``app`` uses the name of the thing being decorated – ``todo``
in this case. Had we called the function something different::

  @app
  def my_todo_app():
     # ... snip ...

  if __name__ == '__main__':
      my_todo_app.main()

.. highlight:: none

the help output would have changed accordingly::

  $ ./todo -h
  usage: my_todo_app [-h]

  optional arguments:
    -h, --help  show this help message and exit

.. highlight:: python

The name can also be manually specified using the ``name`` parameter
to the ``app`` decorator::

  @app(name='supercool-todo-app')
  def todo():
      # ... snip ...

.. highlight:: none

::

   $ ./todo -h
   usage: supercool-todo-app [-h]

   optional arguments:
     -h, --help  show this help message and exit

Typically it's not necessary to manually specify ``name`` for the
``app`` decorator. But later on, when implementing subcommands, the
``name`` parameter makes another appearance, and is extremely useful.
(Think ``./todo list`` – we probably don't want to define our own
function named ``list`` since that is a *very* core built-in….)

.. highlight:: python

Next let's look at the function body::

  def todo():
      yield
      print('Hello, world!')

Technically, ``todo`` is a generator – not a function. At a lower
level this is an important distinction, but for our purposes it
doesn't much matter. What matters are the two "rules" that being a
generator implies:

#. Every clik-decorated function must have at least one ``yield``
   statement.
#. You cannot call clik-decorated functions directly. Well, you can,
   but it's virtually guaranteed to do gnarly and unexpected things.
   Just don't do it.

In terms of program design, the second rule has important
implications. clik programs usually have two layers: an internal API
layer that is responsible for reading / writing / working on data and
a UI layer that uses the internal API and clik to implement the
end-user interface. The internal API shouldn't "know" about clik at
all. (And in the spirit of tutorials everywhere, this advice will be
promptly eschewed because for our demo app the logic will be simple
enough to not warrant any kind of internal API.)

Within our function, there are three phases of execution::

  def todo():
      # configure argument parser
      yield  # give control back to clik, which parses end user arguments
      # do something with parsed arguments

Right now our program has no arguments, so there's no code in the
"configure parser" phase. clik still parses end user arguments (this
is where it handles ``-h`` or errors out on unknown args). And the "do
something" phase is where we print "hello world."

The last bit of code kicks off the whole process::

  if __name__ == '__main__':
      todo.main()

By default, the ``main`` method invokes the application with the
arguments from ``sys.argv``, then calls ``sys.exit`` with the exit
code from the application. You can override these by supplying the
``argv`` and ``exit`` arguments, respectively. (This more advanced
usage will not be covered in the tutorial. These arguments are mainly
provided for testing purposes – to allow test code to invoke the app
with a given set of arguments but not have it exit the process upon
completion.)

Phew, That was a lot of words for twelve lines of code! Let's take a
breather and :ref:`add some help text <tutorial-05-help>` before we
dive into arguments.
