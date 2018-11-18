""" orbital_expressions.py
"""

# Authorship ----------------------------------------------------------------------------------------------------------#
__author__ = "Geoffrey Hyde Garrett"
__copyright__ = None
__credits__ = "Reference [1]"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Geoffrey Hyde Garrett"
__email__ = "g.h.garrett13@gmail.com"
__status__ = "Pre-alpha"

# References ----------------------------------------------------------------------------------------------------------#
# [1] Wakker, K. (2015). Fundamentals of astrodynamics. TU Delft Library. Page 681


# Acknowledgement  ----------------------------------------------------------------------------------------------------#


# Imports  ------------------------------------------------------------------------------------------------------------#
from math import cos, tan, atan, sqrt, acos, atanh, sin, sinh, pi


# Class ---------------------------------------------------------------------------------------------------------------#
class OrbitalExpressions:
    @staticmethod
    def orbit_type(e):
        if e < 1.0:
            return "Elliptical"
        elif e == 1:
            return "Parabolic"
        elif e > 1.0:
            return "Hyperbolic"

    @staticmethod
    def a(r, v, mu):
        return 1 / ((2.0 / r) - (v ** 2 / mu))

    @staticmethod
    def r(p, e, theta):
        return p / (1.0 + e * cos(theta))

    @staticmethod
    def H(mu, a, e):
        return sqrt(mu * a * (1 - e ** 2))

    def n(self, mu, a, e):
        """
        :param mu:
        :param a:
        :param e:
        :return: Mean anomaly (n)
        """
        _orbit_type = self.orbit_type(e)
        if _orbit_type is "Elliptical":
            return sqrt(mu / (a ** 3))
        elif _orbit_type is "Hyperbolic":
            return sqrt(mu / (- a ** 3))
        elif _orbit_type is "Parabolic":
            return sqrt(mu / ((a * (1 - e ** 2)) ** 3))

    def r_p(self, a, e):
        """
        :param a:
        :param e:
        :return: Radius of periapsis (r_p)
        """
        _orbit_type = self.orbit_type(e)
        if _orbit_type is "Elliptical":
            return a * (1 - e)
        elif _orbit_type is "Hyperbolic":
            return (a * (1 - e ** 2)) / 2
        elif _orbit_type is "Parabolic":
            return a * (1 - e)

    def r_a(self, a, e):
        if e < 1.0:
            return a * (1 + e)
        else:
            raise AttributeError(
                "Radius of apoapsis (r_a) cannot be computed for {} trajectory.".format(self.orbit_type(e))
            )

    def theta_max(self, e):
        if e > 1.0:
            return acos(- 1.0 / e)
        else:
            raise AttributeError(
                "θ_max can only be computed for Hyperbolic trajectories. Not applicable to {} trajectory.".format(
                    self.orbit_type(e))
            )

    def E(self, e, theta):
        """
        :param e:
        :param theta:
        :return: Eccentric anomaly (E)
        """
        E = 2 * atan(sqrt((1 - e) / (1 + e)) * tan(theta / 2))
        return E + 2 * pi if E <= 0 else E

    def F(self, e, theta):
        """
        :param e:
        :param theta:
        :return: Hyperbolic anomaly (F)
        """
        F = 2 * atanh(sqrt((e - 1) / (e + 1)) * tan(theta / 2))
        return F + 2 * pi if F <= 0 else F

    def M(self, e, theta):
        """
        :param mu:
        :param a:
        :param t:
        :param tau:
        :return: Mean anomaly (M)
        """
        if e < 1.0:
            M = self.E(e, theta) - e * sin(self.E(e, theta))
            return M + 2 * pi if M <= 0 else M
        elif e > 1.0:
            M = e * sinh(self.F(e, theta)) - self.F(e, theta)
            return M + 2 * pi if M <= 0 else M
        elif e == 1:
            return 0.5 * (tan(theta / 2) + 1.0 / 3 * tan(theta / 2) ** 3)

    def dt(self, e, theta, mu, a):
        return self.M(e, theta) / self.n(mu, a, e)
    # TODO: Complete and add test for dt calculation.

    def tau(self, time, e, theta, mu, a):
        """

        :param time:
        :param e:
        :param theta:
        :param mu:
        :param a:
        :return:
        """
        return time + self.dt(e, theta, mu, a)
    # TODO: Complete and add test for tau calculation.
