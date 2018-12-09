import numpy as np
cimport numpy as np

def racing_car(np.ndarray[np.float64_t] x0, double t, double a):
    """
    INTEG_1
    f (x0) = a m/s/s
    :param x0:
    :param t:
    :param a:
    :return:
    """
    return np.array([x0[1], a])

def point_mass_acceleration_3D(np.ndarray[np.float64_t] x0, double t,
                            double mu):
    """
    INTEG_2
    f (x0) = -μ
             ───⋅r
             |r|^3
    :param x0:
    :param t:
    :param mu:
    :return:
    """
    return np.concatenate((x0[3:6], - mu / (np.linalg.norm(x0[0:3]) ** 3.) * x0[0:3]), axis=None)


def point_mass_acceleration_2D(np.ndarray[np.float64_t] x0, double t,
                            double mu):
    """
    INTEG_2
    f (x0) = -μ
             ───⋅r
             |r|^3
    :param x0:
    :param t:
    :param mu:
    :return:
    """
    return np.concatenate((x0[2:4], - mu / (np.linalg.norm(x0[0:2]) ** 3.) * x0[0:2]), axis=None)
