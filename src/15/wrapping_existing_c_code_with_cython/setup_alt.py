from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("sample", 
              ["sample_alt.pyx"],
              include_dirs=['..'],
              libraries=['sample'],
              runtime_library_dirs=['..'],
              library_dirs=['..'])]
setup(
  name = 'Sample extension module',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
