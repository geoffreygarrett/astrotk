import numpy as np

# "cimport" is used to import special compile-time information
# about the numpy module (this is stored in a file numpy.pxd which is
# currently part of the Cython distribution).
cimport numpy as np

# We now need to fix a datatype for our arrays. I've used the variable
# DTYPE for this, which is assigned to the usual NumPy runtime
# type info object.
DTYPE = np.float

# "ctypedef" assigns a corresponding compile-time type to DTYPE_t. For
# every type in the numpy module there's a corresponding compile-time
# type with a _t-suffix.
ctypedef np.float_t DTYPE_t

# Define a new type for a function-type that accepts a numpy array and
# a double (x0, h) and returns a numpy array (x1).
# cpdef np.ndarray (*f_type)(np.array, np.ndarray)

def step(np.ndarray[np.float64_t] x0, f, double h, t0=0.):
    cdef np.ndarray[np.float64_t] k1 = f(x0, t0)
    cdef np.ndarray[np.float64_t] k2 = f(x0 + h * k1 / 2., t0 + h / 2.)
    cdef np.ndarray[np.float64_t] k3 = f(x0 + h * k2 / 2., t0 + h / 2.)
    cdef np.ndarray[np.float64_t] k4 = f(x0 + h * k3, t0 + h)
    cdef np.ndarray[np.float64_t] st = 1. / 6. * (k1 + 2 * k2 + 2 * k3 + k4)
    return x0 + h * st

# "def" can type its arguments but not have a return type. The type of the
# arguments for a "def" function is checked at run-time when entering the
# function.

# The arrays f, g and h is typed as "np.ndarray" instances. The only effect
# this has is to a) insert checks that the function arguments really are
# NumPy arrays, and b) make some attribute access like f.shape[0] much
# more efficient. (In this example this doesn't matter though.)
def integrate(x0, f, t):
    sol = np.array([x0])
    for idx in range(len(t) - 1):
        _t0 = t[idx]
        sol = np.append(sol, [step(sol[idx], f, h=t[idx + 1] - _t0, t0=_t0)],
                        axis=0)
    return np.array(sol)

def odeint(f, y0, t, args):
    sol = np.array([y0])
    if args:
        if type(args) is float:
            def _f(y, t):
                return f(y, t, args)
        else:
            def _f(y, t):
                return f(y, t, *args)

    for idx in range(len(t) - 1):
        _t0 = t[idx]
        sol = np.append(sol, [step(sol[idx],
                                   _f,
                                   h=t[idx + 1] - _t0,
                                   t0=_t0)], axis=0)
    return np.array(sol)
