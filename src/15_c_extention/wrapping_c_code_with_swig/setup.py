# setup.py
from distutils.core import setup, Extension

setup(name='sample',
      py_modules=['sample.py'],
      ext_modules=[
        Extension('_sample',
                  ['../sample.c', 'sample_wrap.c'],
                  include_dirs = ['..'],
                  define_macros = [],  
                  undef_macros = [],
                  library_dirs = [],
                  libraries = []
                  )
        ]
)
