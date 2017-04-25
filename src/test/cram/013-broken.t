Adds child exceptions to the mix.

  $ alias tap=$TESTDIR/013-broken.py


  $ tap snap
  running setup code
  snap snap snap snap snap
  Traceback (most recent call last):
    File "/home/jjoyce/clik/src/test/cram/013-broken.py", line 46, in <module>
      tap.main()
    File "/home/jjoyce/clik/src/clik/core.py", line 221, in main
      nonzero_rvs = [rv for rv in self._run() if rv != 0]
    File "/home/jjoyce/clik/src/clik/core.py", line 168, in _run
      run_children()
    File "/home/jjoyce/clik/src/clik/core.py", line 150, in run_children
      args._clik_cmd[0]._run(rvs)
    File "/home/jjoyce/clik/src/clik/core.py", line 145, in _run
      rv = next(command._generator)
    File "/home/jjoyce/clik/src/test/cram/013-broken.py", line 41, in snap
      raise Exception('whoops')
  Exception: whoops
  [1]
