#import sys
#sys.path.insert(0, "/usr/local/lib64/python3.6/site-packages")

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(["wss.py"]))
