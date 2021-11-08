pyDhd python module -- 31/10/2013

This is a SWIG generated wrapper for python2 & python3 bindings to dhd. 
Actually, all the standard SDK is implemented, with the sole exception of dhdGetOrientationFrame and dhdGetStatus.
All functions using pointers (dhdGetXXX) returns tuples instead:
  > ret,px,py,pz = dhdGetPosition()
  
It requires libdhd.so (and dhd.h) installed system-wide. 
It uses python-distutils. To build and install simply use:
  $ python[3] setup.py clean
  $ python[3] setup.py build
  $ sudo python[3] setup.py install

Tested w/ python2.7, python3.3 and dhd-sdk-3.5 on Fedora 19 as of October 2013
It is not tested on other platforms, but should theoretically work. The author would appreciate to know if it's the case (or not).
