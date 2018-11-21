"""
assignment_1_b2.py
"""
from astrotk.AE4878.bodies import Earth
from astrotk.twobody.state import vector
from astrotk.twobody.state import classical
from astrotk.tests.test_state_values import *

"""
Question 1
"""
# Values are given their respective units during VectorState object construction.
x = 10157768.1264
y = -6475997.0091
z = 2421205.9518
xdot = 1099.2953996
ydot = 3455.1059240
zdot = 4355.0978095

# Instantiate VectorState object with given Cartesian components.
vector_state_1 = vector.VectorState(
    attractor=Earth(),  # Earth object defined in bodies.py
    r_vec=np.array([x, y, z]) * u.m,
    v_vec=np.array([xdot, ydot, zdot]) * u.m / u.s
)

# Print ClassicalState LaTeX table (for given table).
# print(vector_state_1.latex(30))

# Convert VectorState object into ClassicalState object.
classical_state_1 = vector_state_1.to_classical()

# Print ClassicalState LaTeX table.
print(classical_state_1.latex(20))

"""
Question 2
"""
# All values are given their respective units. (u.km, u.cm, u.mm, u.rad, all possible and pass tests)
a = 12269687.5912 * u.m
e = 0.004932091570 * u.dimensionless_unscaled
i = 109.823277603 * u.deg
raan = 134.625563565 * u.deg
argp = 106.380426142 * u.deg
M = 301.149932402 * u.deg

# Instantiate ClassicalState object with given Classical orbital elements.
classical_state_2 = classical.ClassicalState(
    attractor=Earth(),  # Earth object defined in bodies.py
    a=a,
    e=e,
    inc=i,
    raan=raan,
    argp=argp,
    M=M
)

# Convert ClassicalState object into VectorState object.
vector_state_2 = classical_state_2.to_vectors()

# Print VectorState LaTeX table.
print(vector_state_2.latex(10))

