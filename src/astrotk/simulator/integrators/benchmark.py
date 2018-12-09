import astrotk.simulator.integrators.RK4 as RK4
import astrotk.simulator.integrators.Euler as Euler
from astrotk.simulator.eom.test import racing_car as cy_racing_car
from astrotk.simulator.eom.test import point_mass_acceleration_2D as cy_point_mass_acceleration
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


# def odeint(f, y0, t, args):


def python_test(t_s, integrator, eom, y0, args):
    now = time.time()
    sol = integrator(eom, y0, t_s, args=args)
    tt = time.time() - now
    print("Python time taken --- : {}".format(tt))
    return sol


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    ts_car = np.linspace(0, 60., 50000)

    # y0_car = np.array([0.0, 0.0])
    # py = python_test(ts, odeint, racing_car, y0_car)[:, 0]
    # cy = cython_test(ts, Euler, cy_racing_car, y0_car)[:, 0]
    #
    import astropy.units as u

    D = 86164.1004  # s
    mu = 398600.441 * u.km ** 3 / u.s / u.s
    print(mu.si)
    a = ((D / (2 * np.pi))**2 * mu.si.value) ** (1. / 3.)
    print(a)
    a = a * u.m
    print(a.to(u.km))
    v = np.sqrt(mu / a)

    # y0_sat = np.array([a.to(u.km).value, 0, 0, 0, v.to(u.km/u.s).value, 0])
    y0_sat = np.array([a.to(u.km).value, 0, 0, v.to(u.km/u.s).value])

    step_size = 6200
    time_simulated = 24*3600 *30
    ts_sat = np.arange(0., time_simulated, step_size)
    cy = cython_test(ts_sat, RK4, cy_point_mass_acceleration, y0_sat, args=mu.to(u.km**3/u.s/u.s).value)
    time__ = time_simulated * u.s

    plt.title(("Duration: {} hrs".format(time__.to(u.hour).value) + "    " +"$ \delta$t = {} s".format(step_size) +
               "    Method: RK4"))
    plt.plot(cy[:, 0], cy[:, 1], label="Cython")
    plt.ylabel('y-coordinate [m]')
    # plt.grid()
    plt.axis('equal')
    plt.xlabel('x-coordinate [m]')
    plt.legend()
    plt.show()

    # plt.loglog(ts_sat, (py - cy) / py)
    # plt.show()
    # TODO: Create .rst for conclusion of Cythonized integration functions.
