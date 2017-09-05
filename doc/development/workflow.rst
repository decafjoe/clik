
==========
 Workflow
==========

.. note::

   Clik is currently maintained by a single person. For now, I don't
   want to put any hard and fast rules on how development should be
   done. What follows is a sketch.

**All commits to master must be stable, working, QA-ed code.** That
is, every commit must:

* Be free of linter violations
* Pass the full test suite on all supported interpreters
* Maintain 100% code coverage (exceptions may be made)
* Document the changes appropriately (in end user documentation,
  docstrings, developer documentation, etc)
* Have a descriptive commit message
* Be reviewed by a project committer [0]_

**Development must happen off-master.** In other words, you should
*never be committing or pushing directly to master.*

Once the patch is working, **history must be rewritten to read
logically, and must be rebased off of the current master.** Again,
this should be done off-master. Remember rule #1: all commits to
master must be stable, working, QA-ed code.

With the patch and history ready, **submit a pull request**. This will
automatically start a Travis CI run to check for linter violations or
test failures. If the test run passes, a clik committer will review
your changes for a possible merge into master.

.. note::

   After some quick Googling, I can't find a quick way to have Travis
   run the tests against every commit in a pull request. So I guess
   for now, multi-commit pull requests must be tested/linted locally
   commit-by-commit? Ugh.

.. [0] Obviously, I review my own code at this time. This is not
       ideal, but will have to suffice unless/until clik gets another
       committer.
