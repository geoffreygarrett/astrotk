""" classical.py
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
# [1] Juanlu001 et al., poliastro, (2018), GitHub repository, https://github.com/poliastro/poliastro


# Acknowledgement  ----------------------------------------------------------------------------------------------------#
# Style and structure was inspired from poliastro, a tool I spent the entirety of my bachelor's thesis using for
# interplanetary trajectories to Pluto.

# Imports -------------------------------------------------------------------------------------------------------------#
from ._base import BaseState
import astropy.units as u
from astrotk.twobody.utils import vector2spherical
from astrotk.twobody.utils import classical2vector
from astrotk.twobody.utils import OrbitalExpressions
from astrotk.twobody.state import spherical
from astrotk.twobody.state import vector


# Class ---------------------------------------------------------------------------------------------------------------#
class ClassicalState(BaseState):
    def __init__(self, attractor, a, e, inc, raan, argp, theta=None, **kwargs):
        """
        Two-body problem classical state representation, to be inherited by other state representations. Attractor must
        be defined as the geometry of the state is only transformable to another representation given the constant mu.
        :param attractor:
        """
        super().__init__(attractor)
        self._a = a
        self._e = e
        self._inc = inc
        self._raan = raan
        self._argp = argp
        if theta is not None:
            self._theta = theta
        else:
            try:
                self._theta = OrbitalExpressions().theta(self._e.value, kwargs["M"].si.value) * u.rad
            except KeyError:
                raise SystemError("If theta is not defined then M must be for instantiation of ClassicalState.")

    # Property overrides ----------------------------------------------------------------------------------------------#
    @property
    def a(self):
        """
        :return: <astropy.units.Quantity> Semi-major axis (a)
        """
        return self._a

    @property
    def e(self):
        """
        :return: <astropy.units.Quantity> Eccentricity (e)
        """
        return self._e

    @property
    def inc(self):
        """
        :return: <astropy.units.Quantity> Inclination angle (i)
        """
        return self._inc

    @property
    def raan(self):
        """
        :return: <astropy.units.Quantity> Right ascension of ascending node (Ω)
        """
        return self._raan

    @property
    def argp(self):
        """
        :return: <astropy.units.Quantity> Argument of periapsis (ω)
        """
        return self._argp

    @property
    def theta(self):
        """
        :return: <astropy.units.Quantity> True anomaly (θ)
        """
        return self._theta

    # Method updates --------------------------------------------------------------------------------------------------#
    def to_vectors(self):
        r, v = classical2vector(self._a.to(u.m).value,
                                self._e.to(u.dimensionless_unscaled).value,
                                self._inc.to(u.rad).value,
                                self._raan.to(u.rad).value,
                                self._argp.to(u.rad).value,
                                self._theta.to(u.rad).value,
                                self._attractor.mu.to(u.m ** 3 / u.s / u.s).value)
        return vector.VectorState(self._attractor, r * u.m, v * u.m / u.s)

    def to_spherical(self):
        r, ra, de, v, fpa, azi = vector2spherical(
            *classical2vector(self._a.to(u.m).value,
                              self._e.to(u.dimensionless_unscaled).value,
                              self._inc.to(u.rad).value,
                              self._raan.to(u.rad).value,
                              self._argp.to(u.rad).value,
                              self._theta.to(u.rad).value,
                              self._attractor.mu.to(u.m ** 3 / u.s / u.s).value)
        )
        return spherical.SphericalState(self._attractor,
                                        r * u.m,
                                        ra * u.rad,
                                        de * u.rad,
                                        v * u.m / u.s,
                                        fpa * u.rad,
                                        azi * u.rad)

    def to_classical(self):
        return self
