#include <stdio.h>
#include <Python.h>

static PyObject *py_die(PyObject *self, PyObject *args) {
  char *s = 0;

  *s = 'x';
  Py_RETURN_NONE;
}


/* Module method table */
static PyMethodDef SampleMethods[] = {
  {"die",  py_die, METH_VARARGS},
  { NULL, NULL, 0, NULL}
};

/* Module structure */
static struct PyModuleDef samplemodule = {
  PyModuleDef_HEAD_INIT,
  "sample",           /* name of module */
  "A sample module",  /* Doc string (may be NULL) */
  -1,                 /* Size of per-interpreter state or -1 */
  SampleMethods       /* Method table */
};

/* Module initialization function */
PyMODINIT_FUNC
PyInit_sample(void) {
  return PyModule_Create(&samplemodule);
}
