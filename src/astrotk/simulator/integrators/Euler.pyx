import numpy as np
cimport numpy as np

def step(np.ndarray[np.float64_t] x0, f, h=1., t0=0.):
    st = f(x0, t0)
    return x0 + h * st

def integrate(f, np.ndarray[np.float64_t] y0, t):
    sol = np.array([y0])
    _f = f()
    for idx in range(len(t) - 1):
        _t0 = t[idx]
        sol = np.append(sol, [step(sol[idx], f, h=t[idx + 1] - _t0, t0=_t0)],
                        axis=0)
    return np.array(sol)

def odeint(f, np.ndarray[np.float64_t] y0, t, args):
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
