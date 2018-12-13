import time

import numpy as np


def step(x0, f, h=1., t0=0.):
    k1 = f(x0, t0)
    k2 = f(x0 + h * k1 / 2., t0 + h / 2.)
    k3 = f(x0 + h * k2 / 2., t0 + h / 2.)
    k4 = f(x0 + h * k3, t0 + h)
    st = 1. / 6. * (k1 + 2 * k2 + 2 * k3 + k4)
    return x0 + h * st


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


def racing_car(y, t, a):
    """
    f (x0) = 2.0 m/s/s
    :param t0:
    :param x0:
    :return:
    """
    # print(t0)
    return np.array([y[1], a])


def integ_2(y, t, mu):
    """
    f (x0) = -μ
             ───⋅r
             |r|^3
    :param t0:
    :param x0:
    :param mu:
    :return:
    """
    return np.concatenate((y[3:6], - mu / (np.linalg.norm(y[0:3]) ** 3.) * y[0:3]))


def cython_test(t_s, integrator, eom, y0, args):
    now = time.time()
    sol = integrator.odeint(eom, y0, t_s, args=args)
    tt = time.time() - now
    print("Cython time taken: {}".format(tt))
    return sol


def python_test(t_s, integrator, eom, y0, args):
    now = time.time()
    sol = integrator(eom, y0, t_s, args=args)
    tt = time.time() - now
    print("Python time taken --- : {}".format(tt))
    return sol
