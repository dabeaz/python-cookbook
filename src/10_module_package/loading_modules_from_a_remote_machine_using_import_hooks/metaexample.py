# metaexample.py
#
# Example of using a meta-path importer

# Enable for debugging
if False:
    import logging
    logging.basicConfig(level=logging.DEBUG)

import urlimport
urlimport.install_meta('http://localhost:15000')

import fib
import spam
import grok.blah
print(grok.blah.__file__)
