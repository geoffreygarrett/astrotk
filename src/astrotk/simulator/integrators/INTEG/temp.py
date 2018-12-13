import numpy as np
from astrotk.simulator.eom.test import point_mass_acceleration_3D

from astrotk.bodies.bodies import Earth
from astrotk.simulator.integrators import Euler
from astrotk.simulator.integrators import RK4
from astrotk.simulator.integrators.INTEG.common import propagate2
from astrotk.twobody.utils.transformation import classical2vector

# NUMERICAL EXAMPLE EULER TABLE
ex_a = 7378137  # km
ex_e = 0.1  # -
ex_i = 0.  # rad
ex_raan = 0.  # rad
ex_argp = 0.  # rad
ex_thet = 0.  # rad
ex_step_siz = 10.  # s

ex_r, ex_v = classical2vector(a=ex_a,
                              e=ex_e,
                              inc=ex_i,
                              raan=ex_raan,
                              argp=ex_argp,
                              theta=ex_thet,
                              mu=Earth.mu.si.value)

ex_t = np.array([0, 10., 20.])

ex_arg = {
    "t": ex_t,
    "eom": point_mass_acceleration_3D,
    "y0": np.concatenate((ex_r, ex_v)),
    "args": Earth.mu.si.value
}

x0, x1, x2 = propagate2(Euler, ex_arg).round(3)

import pandas as pd

df = pd.DataFrame({
    "x_0": x0,
    "x_1": x1,
    "x_2": x2
})

print(df.to_latex(index=False))

x0rk, x1rk, x2rk = propagate2(RK4, ex_arg).round(3)

df2 = pd.DataFrame({
    "x_0": x0rk,
    "x_1": x1rk,
    "x_2": x2rk
})

print(df2.to_latex(index=False))
