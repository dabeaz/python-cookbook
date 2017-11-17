# Example of path-path import hook

# Enable for debugging
if False:
    import logging
    logging.basicConfig(level=logging.DEBUG)

import urlimport
urlimport.install_path_hook()

import sys
sys.path.append('http://localhost:15000')

import fib
import spam
import grok.blah
print(grok.blah.__file__)

