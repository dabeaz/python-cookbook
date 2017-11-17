# setup.py
from distutils.core import setup, Extension

setup(name="sample", 
      ext_modules=[
        Extension("sample",
                  ["../sample.c", "pysample.c"],
                  include_dirs = ['..'],
                  )
        ]
)
