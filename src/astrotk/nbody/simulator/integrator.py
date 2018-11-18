import numpy as np


def one_equation_explicit_1(Y0, dY, dt):
    Y1 = Y0 + np.multiply(dY, dt)
    return Y1


def one_equation_explicit_2(Y0, dY, dt):
    Y11 = Y0 + np.multiply(dY, dt)
    Y01 = Y0 + 0.5 * np.multiply(dY, dt)
    dY01 = np.divide((Y11 - Y01), 0.5)
    Y1 = Y0 + dt * dY01
    return Y1
