from collections import namedtuple
import numpy as np

keplerian_state = namedtuple('keplerian_state', ['argp', 'raan', 'inc', 'r'])
cartesian_state = namedtuple('cartesian_state', ['x', 'y', 'z'])
spherical_state = namedtuple('spherical_state', ['r', 'lon', 'lat'])


def spherical2cartesian(_spherical_state):
    _cartesian_state   = cartesian_state
    _cartesian_state.x = _spherical_state.r * np.cos(_spherical_state.lat) * np.cos(_spherical_state.lon)
    _cartesian_state.y = _spherical_state.r * np.cos(_spherical_state.lat) * np.sin(_spherical_state.lon)
    _cartesian_state.z = _spherical_state.r * np.sin(_spherical_state.lat)
    return _cartesian_state


def cartesian2spherical(_cartesian_state):
    _spherical_state     = spherical_state
    _spherical_state.r   = np.sqrt(_cartesian_state.x ** 2 + _cartesian_state.y ** 2 + _cartesian_state.z ** 2)
    _r_xy                = np.sqrt(_cartesian_state.x ** 2 + _cartesian_state.y ** 2)
    _spherical_state.lon = np.arctan2(_cartesian_state.y / _r_xy, _cartesian_state.x / _r_xy)
    _spherical_state.lat = np.arcsin(_cartesian_state.z / _spherical_state.r)
    return _spherical_state


def keplerian2cartesian(_keplerian_state):
    _keplerian_state = keplerian_state
    
