
===========
 Internals
===========


clik
====

.. automodule:: clik

.. autodata:: clik.__version__


clik.app
========

.. automodule:: clik.app
   :members: current_app, parser, args, g, run_children
.. autofunction:: clik.app.app
.. autoclass:: clik.app.AttributeDict
   :show-inheritance:
   :members: __getattr__, __setattr__, __delattr__
.. autoclass:: clik.app.App
   :show-inheritance:
   :members:


clik.argparse
=============

.. automodule:: clik.argparse
.. autoexception:: clik.argparse.ArgumentParserExit
   :members:
.. autoexception:: clik.argparse.BareUnsupportedFeatureError
   :members:
.. autoclass:: clik.argparse.HelpFormatter
   :show-inheritance:
.. autoclass:: clik.argparse.ArgumentParser
   :show-inheritance:
   :members:
   :private-members:


clik.command
============

.. automodule:: clik.command
   :members: catch, ARGS, STACK, SHOW_SUBCOMMANDS
.. autoexception:: clik.command.BareAlreadyRegisteredError
   :members:
.. autoclass:: clik.command.Command
   :show-inheritance:
   :members: _ctx, _parser, _name, _aliases, _fn, _generator, _parent,
             _children, _bare

   .. automethod:: __init__
   .. automethod:: __call__
   .. automethod:: _configure_parser
   .. automethod:: _check_bare_arguments
   .. automethod:: _run


clik.compat
===========

.. automodule:: clik.compat
.. autodata:: clik.compat.PY2
   :annotation:
.. autodata:: clik.compat.PY26
   :annotation:
.. autodata:: clik.compat.PY33
   :annotation:


clik.context
============

.. automodule:: clik.context
.. autoexception:: clik.context.LockedMagicError
   :members:
.. autoexception:: clik.context.MagicNameConflictError
   :members:
.. autoexception:: clik.context.UnregisteredMagicNameError
   :members:
.. autoexception:: clik.context.UnboundMagicError
   :members:
.. autoclass:: clik.context.Context
   :show-inheritance:
   :members:
   :special-members: __call__


clik.magic
==========

.. automodule:: clik.magic
.. autoclass:: clik.magic.Magic
