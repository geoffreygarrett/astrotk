""" vector.py
"""
"""
Authorship
"""
__author__ = "Geoffrey Hyde Garrett"
__copyright__ = None
__credits__ = "Reference [1]"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Geoffrey Hyde Garrett"
__email__ = "g.h.garrett13@gmail.com"
__status__ = "Pre-alpha"

"""
# [1] Juanlu001 et al., poliastro, (2018), GitHub repository, https://github.com/poliastro/poliastro
"""

"""
Acknowledgments
# Style and structure was inspired from poliastro, a tool I spent the entirety of my bachelor's thesis using for
# interplanetary trajectories to Pluto.
"""

"""
Imports
"""
from ._base import BaseState
import astropy.units as u
from astrotk.twobody.utils import vector2classical
from astrotk.twobody.utils import vector2spherical
from astrotk.twobody.state import classical
from astrotk.twobody.state import spherical


class VectorState(BaseState):
    def __init__(self, attractor, r_vec, v_vec):
        """
        Two-body problem vector state representation. Attractor must be defined as the geometry of the state is only
        transformable to another representation given the constant mu.
        :param attractor:
        """
        super().__init__(attractor)
        self._r_vec = r_vec
        self._v_vec = v_vec

    """
    Property overrides
    """
    @property
    def r_vec(self):
        """
        :return: <astropy.units.Quantity> Cartesian vector representation of position (r_vec)
        """
        return self._r_vec

    @property
    def v_vec(self):
        """
        :return: <astropy.units.Quantity> Cartesian vector representation of velocity (v_vec)
        """
        return self._v_vec

    """
    Method overrides
    """
    def to_vectors(self):
        return self

    def to_spherical(self):
        radius, ra, de, v, fpa, azi = vector2spherical(self._r_vec.to(u.m).value,
                                                       self._v_vec.to(u.m / u.s).value)
        return spherical.SphericalState(self._attractor,
                                        radius * u.m,
                                        ra * u.rad,
                                        de * u.rad,
                                        v * u.m / u.s,
                                        fpa * u.rad,
                                        azi * u.rad)

    def to_classical(self):
        a, e, inc, raan, argp, theta = vector2classical(
            self._r_vec.to(u.m).value,
            self._v_vec.to(u.m / u.s).value,
            self._attractor.mu.to(u.m ** 3 / u.s / u.s).value
        )
        return classical.ClassicalState(self._attractor,
                                        a * u.m,
                                        e * u.dimensionless_unscaled,
                                        inc * u.rad,
                                        raan * u.rad,
                                        argp * u.rad,
                                        theta * u.rad)
