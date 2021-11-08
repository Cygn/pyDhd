#!/usr/bin/env python

"""
setup.py file for SWIG
"""

from distutils.core import setup, Extension


pyDhd_module = Extension('_pyDhd',
                           sources=['pyDhd_wrap.cxx'],
                           libraries=['dhd', 'usb-1.0']
                           )

setup (name = 'pyDhd',
       version = '0.1',
       author      = "Sinan HALIYO",
       description = """dhd Python interface""",
       ext_modules = [pyDhd_module],
       py_modules = ["pyDhd"],
       )
