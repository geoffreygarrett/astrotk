import numpy as np

from .orbital_expressions import OrbitalExpressions


def spherical2vector(radius, ra, de, v, fpa, azi):
    """
    :param _spherical_state:
    :return:
    """
    _r = radius
    _cos_de = np.cos(de)
    _sin_de = np.sin(de)
    _cos_ra = np.cos(ra)
    _sin_ra = np.sin(ra)
    _x = _r * _cos_de * _cos_ra
    _y = _r * _cos_de * _sin_ra
    _z = _r * _sin_de

    return np.array([_x, _y, _z]), np.array([1.0, 1.0, 1.0])
    # raise NotImplementedError("Haven't transformed the velocity yet.")
    # return VectorState(_x, _y, _z, _v_x, _v_y, _v_z)


def vector2spherical(r, v):
    _r = np.linalg.norm(r)
    _r_xy = np.sqrt(r[0] ** 2 + r[1] ** 2)
    _v_xy = np.sqrt(v[0] ** 2 + v[1] ** 2)
    _ra = np.arctan2(r[1] / _r_xy, r[0] / _r_xy)
    _de = np.arcsin(r[2] / _r)
    _v = np.linalg.norm(v)
    _fpa = np.arcsin(np.dot(r, v) / (_r * _v))
    _azi = np.arctan2(v[0] / _v_xy, v[1] / _v_xy)
    return _r, _ra, _de, _v, _fpa, _azi


def classical2vector(a, e, inc, raan, argp, theta, mu):
    _cos_raan = np.cos(raan)
    _sin_raan = np.sin(raan)
    _cos_argp = np.cos(argp)
    _sin_argp = np.sin(argp)
    _cos_inc = np.cos(inc)
    _sin_inc = np.sin(inc)
    _theta = theta
    _r = OrbitalExpressions().r(a * (1 - e ** 2), e, theta)  # TODO: Check
    _e = e

    _l1 = (_cos_raan * _cos_argp - _sin_raan * _sin_argp * _cos_inc)
    _l2 = (-_cos_raan * _sin_argp - _sin_raan * _cos_argp * _cos_inc)
    _m1 = (_sin_raan * _cos_argp + _cos_raan * _sin_argp * _cos_inc)
    _m2 = (-_sin_raan * _sin_argp + _cos_raan * _cos_argp * _cos_inc)
    _n1 = _sin_argp * _sin_inc
    _n2 = _cos_argp * _sin_inc

    _aux = np.array([_r * np.cos(_theta), _r * np.sin(_theta)]).T
    _transformation = np.array([[_l1, _l2],
                                [_m1, _m2],
                                [_n1, _n2]])

    # Position
    _xyz = np.matmul(_transformation, _aux)
    _x = _xyz[0]
    _y = _xyz[1]
    _z = _xyz[2]

    # Velocity
    _H = OrbitalExpressions().H(mu, a, e)
    _v_x = mu / _H * (-_l1 * np.sin(_theta) + _l2 * (_e + np.cos(_theta)))
    _v_y = mu / _H * (-_m1 * np.sin(_theta) + _m2 * (_e + np.cos(_theta)))
    _v_z = mu / _H * (-_n1 * np.sin(_theta) + _n2 * (_e + np.cos(_theta)))
    return np.array([_x, _y, _z]), np.array([_v_x, _v_y, _v_z])


def vector2classical(r, v, mu):
    _r = np.linalg.norm(r)
    _v = np.linalg.norm(v)
    _h = np.cross(r, v)
    _N = np.cross(np.array([0, 0, 1]).T, _h)
    _N_xy = np.sqrt(_N[0] ** 2 + _N[1] ** 2)
    _a = OrbitalExpressions().a(_r, _v, mu)
    _e_vec = (np.cross(v, _h) / mu) - (r / _r)
    _e = np.linalg.norm(_e_vec)
    _inc = np.arccos(_h[-1] / np.linalg.norm(_h))
    _raan = np.arctan2(_N[1] / _N_xy, _N[0] / _N_xy)

    _s1 = 1 if np.dot(np.cross(_N / np.linalg.norm(_N), _e_vec), _h) > 0 else -1
    _argp = _s1 * np.arccos(
        np.dot(_e_vec / np.linalg.norm(_e_vec),
               _N / np.linalg.norm(_N))
    )

    _s2 = 1 if np.dot(np.cross(_e_vec, r), _h) > 0 else -1
    _theta = _s2 * np.arccos(
        np.dot(
            r / np.linalg.norm(r),
            _e_vec / np.linalg.norm(_e_vec))
    )

    _theta = 2 * np.pi + _theta if _theta <= 0 else _theta
    _raan = 2 * np.pi + _raan if _raan <= 0 else _raan
    _argp = 2 * np.pi + _argp if _argp <= 0 else _argp

    return _a, _e, _inc, _raan, _argp, _theta
