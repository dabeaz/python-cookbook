import ctypes
lib = ctypes.cdll.LoadLibrary(None)

# Get the address of sin() from the C math library
addr = ctypes.cast(lib.sin, ctypes.c_void_p).value
print(addr)
140735505915760

# Turn the address into a callable function
functype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
func = functype(addr)
print(func)

# Call the resulting function
print(func(2))
print(func(0))
