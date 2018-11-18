""" spherical.py
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
from astrotk.twobody.utils import vector2classical
from astrotk.twobody.utils import spherical2vector
from astrotk.twobody.state import classical
from astrotk.twobody.state import vector


# Class ---------------------------------------------------------------------------------------------------------------#
class SphericalState(BaseState):
    def __init__(self, attractor, radius, ra, de, v, fpa, azi):
        """
        Two-body problem spherical state representation. Attractor must be defined as the geometry of the state is only
        transformable to another representation given the constant mu.
        :param attractor:
        """
        super().__init__(attractor)
        self._radius = radius
        self._ra = ra
        self._de = de
        self._v = v
        self._fpa = fpa
        self._azi = azi

    # Property overrides ----------------------------------------------------------------------------------------------#
    @property
    def radius(self):
        """
        :return: <astropy.units.Quantity> Radius or position vector magnitude (|r_vec|)
        """
        return self._radius

    @property
    def ra(self):
        """
        :return: <astropy.units.Quantity> Right ascension angle (α)
        """
        return self._ra

    @property
    def de(self):
        """
        :return: <astropy.units.Quantity> Declination (δ)
        """
        return self._de

    @property
    def v(self):
        """
        :return: <astropy.units.Quantity> Velocity magnitude (|v_vec|)
        """
        return self._v

    @property
    def fpa(self):
        """
        :return: <astropy.units.Quantity> Flight path angle (γ)
        """
        return self._fpa

    @property
    def azi(self):
        """
        :return: <astropy.units.Quantity> Azimuth angle (ψ)
        """
        return self._azi

    # Method updates --------------------------------------------------------------------------------------------------#
    def to_vectors(self):
        r_vec, v_vec = spherical2vector(self._radius.to(u.m).value,
                                        self._ra.to(u.dimensionless_unscaled).value,
                                        self._de.to(u.rad).value,
                                        self._v.to(u.rad).value,
                                        self._fpa.to(u.rad).value,
                                        self._azi.to(u.rad).value)
        return vector.VectorState(self._attractor, r_vec * u.m, v_vec * u.m / u.s)

    def to_spherical(self):
        return self

    def to_classical(self):
        a, e, inc, raan, argp, theta = vector2classical(
            *spherical2vector(self._radius.to(u.m).value,
                              self._ra.to(u.dimensionless_unscaled).value,
                              self._de.to(u.rad).value,
                              self._v.to(u.rad).value,
                              self._fpa.to(u.rad).value,
                              self._azi.to(u.rad).value)
        )
        return classical.ClassicalState(self._attractor,
                                        a * u.m,
                                        e * u.dimensionless_unscaled,
                                        inc * u.rad,
                                        raan * u.rad,
                                        argp * u.rad,
                                        theta * u.rad)
