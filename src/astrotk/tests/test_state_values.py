import astropy.units as u
import numpy as np

Test1Classical = [
    6787746.891 * u.m,
    0.000731104 * u.dimensionless_unscaled,
    51.68714486 * u.deg,
    127.5486706 * u.deg,
    74.21987137 * u.deg,
    24.10027677 * u.deg,
    24.08317766 * u.deg,
    24.06608426 * u.deg
]
Test1Vector = [
    np.array([
        -2700816.14,
        -3314092.80,
        5266346.42,
    ]) * u.m,
    np.array([
        5168.606550,
        -5597.546618,
        -868.878445
    ]) * u.m / u.s
]

Test2Classical = [
    7096137.00 * u.m,
    0.0011219 * u.dimensionless_unscaled,
    92.0316 * u.deg,
    296.1384 * u.deg,
    120.6878 * u.deg,
    239.5437 * u.deg,
    239.5991 * u.deg,
    239.6546 * u.deg
]
Test2Vector = [
    np.array([
        3126974.99,
        -6374445.74,
        28673.59,
    ]) * u.m,
    np.array([
        -254.91197,
        -83.30107,
        7485.70674
    ]) * u.m / u.s
]
