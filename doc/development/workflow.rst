
==========
 Workflow
==========

.. note::

   Clik is currently maintained by a single person. For now, I don't
   want to put any hard and fast rules on how development should be
   done. What follows is a sketch.

**Master must always be stable, working, QA-ed code.** That is, at all
times master must:

* Be free of linter violations
* Pass the full test suite on all supported interpreters
* Maintain 100% code coverage (exceptions may be made)
* Contain approprite documentation for any changes (in end user
  documentation, docstrings, developer documentation, etc)
* Have a descriptive commit messages

**Development must happen off-master.** In other words, you should
almost *never be committing or pushing directly to master.*

Once the patch is working, **history must be rewritten to be linear
and neat, and must be rebased off of the current master.** Group
changes logically. Larger groups of smaller commits are preferable to
smaller groups of larger commits.

With the patch and history ready, **submit a pull request**. The pull
request must provide a general description of the change and the
rationale for why clik needs the code. Commit messages are the "what",
pull request messages are the "why".

Submitting a pull request will automatically start a Travis CI run to
check for linter violations or test failures. If the test run passes,
a clik committer will review your changes for a possible merge into
master.
