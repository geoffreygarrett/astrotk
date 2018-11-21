""" _base.py
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
References
# [1] Juanlu001 et al., poliastro, (2018), GitHub repository, https://github.com/poliastro/poliastro
"""

"""
Acknowledgements
# Style and structure was inspired from poliastro, a tool I spent the entirety of my bachelor's thesis using for
# interplanetary trajectories to Pluto.
"""

"""
Imports 
"""
from astrotk.twobody.utils import OrbitalExpressions
from astrotk.twobody.utils import formatting
import astropy.units as u


class BaseState(object):
    """
    Private BaseState class is defined to provide Classical, Spherical and Vector elements as accessible to all children
    classes. This specific style is adapted from [1] and proves to be highly effective for higher level analysis in
    Python. This BaseState belongs to the astrotk/twobody module and thus can only be used as such.
    """
    def __init__(self, attractor):
        """
        :param attractor: astrotk.AE4878.bodies._Body() object.
        TODO: Create a general module that defines characteristics of all bodies in the Solar System.
        """
        self._attractor = attractor

    def _get_state_values(self):
        """
        :return: Returns a astropy.Quantities list of all parameters defining the current state type.
        TODO: Bring this code into another helper script.
        """
        temp = self.__dict__
        temp.pop('_orbital_expressions')
        temp.pop('_attractor')
        keys = list(temp.keys())
        return [temp[keys[i]] for i in range(len(keys))]

    """
    Cartesian vectors
    """
    @property
    def r_vec(self):
        """
        Position vector (r)
        :return:
        """
        return self.to_vectors().r

    @property
    def v_vec(self):
        """
        Velocity vector (v)
        :return:
        """
        return self.to_vectors().v

    """
    Spherical components
    """
    @property
    def radius(self):
        """
        :return: <astropy.units.Quantity> Radius or position vector magnitude (|r_vec|)
        """
        return self.to_spherical().radius

    @property
    def ra(self):
        """
        :return: <astropy.units.Quantity> Right ascension angle (α)
        """
        return self.to_spherical().ra

    @property
    def de(self):
        """
        :return: <astropy.units.Quantity> Declination (δ)
        """
        return self.to_spherical().de

    @property
    def v(self):
        """
        :return: <astropy.units.Quantity> Velocity magnitude (|v_vec|)
        """
        return self.to_spherical().v

    @property
    def fpa(self):
        """
        :return: <astropy.units.Quantity> Flight path angle (γ)
        """
        return self.to_spherical().fpa

    @property
    def azi(self):
        """
        :return: <astropy.units.Quantity> Azimuth angle (ψ)
        """
        return self.to_spherical().azi

    """
    Classical orbital elements
    """
    @property
    def a(self):
        """
        :return: <astropy.units.Quantity> Semi-major axis (a)
        """
        return self.to_classical().a

    @property
    def e(self):
        """
        :return: <astropy.units.Quantity> Eccentricity (e)
        """
        return self.to_classical().e

    @property
    def inc(self):
        """
        :return: <astropy.units.Quantity> Inclination angle (i)
        """
        return self.to_classical().inc

    @property
    def raan(self):
        """
        :return: <astropy.units.Quantity> Right ascension of ascending node (Ω)
        """
        return self.to_classical().raan

    @property
    def argp(self):
        """
        :return: <astropy.units.Quantity> Argument of periapsis (ω)
        """
        return self.to_classical().argp

    @property
    def theta(self):
        """
        :return: <astropy.units.Quantity> True anomaly (θ)
        """
        return self.to_classical().theta

    """
    Other Classical orbital elements
    """
    @property
    def r_p(self):
        """
        :return: <astropy.units.Quantity> Radius of periapsis (r_p)
        """
        # TODO: Add an error exception/catch for Hyperbolic & Parabolic orbits.
        return OrbitalExpressions().r_p(self.a.to(u.m).value, self.e.to(u.dimensionless_unscaled).value) * u.m

    @property
    def r_a(self):
        """
        :return: <astropy.units.Quantity> Radius of apoapsis (r_a)
        """
        return OrbitalExpressions().r_a(self.a.to(u.m).value, self.e.to(u.dimensionless_unscaled).value) * u.m

    @property
    def tau(self, time_now=None):
        """
        :return: <astropy.units.Quantity> Time of periapsis passage (τ)
        """
        # TODO: Determine the time system to be used. (consider use of astropy.time.Time(scale=tdb))
        return OrbitalExpressions().tau(time_now, self.e, self.theta, self._attractor.mu, self.a) * u.s

    @property
    def E(self):
        """
        :return: <astropy.units.Quantity> Eccentric anomaly (E)
        """
        try:
            return OrbitalExpressions().E(self.e.value, theta=self.theta.value) * u.rad
        except AttributeError:
            return OrbitalExpressions().E(self.e.value, M=self.M.value) * u.rad

    @property
    def M(self):
        """
        :return: <astropy.units.Quantity> Mean anomaly (M)
        """
        return OrbitalExpressions().M(self.e.value, self.theta.value) * u.rad

    """
    Print format options
    """
    def prettytable(self):
        return formatting.prettytable_state(self)

    def prettyprint(self):
        print(self.prettytable())

    def latex(self):
        return formatting.latex(self)


    """
    Method placeholders to be overwritten by children classes.
    """
    def to_vectors(self):
        raise NotImplementedError("{} is not a standalone object; purpose = inheritance.".format(type(self).__name__))

    def to_spherical(self):
        raise NotImplementedError("{} is not a standalone object; purpose = inheritance.".format(type(self).__name__))

    def to_classical(self):
        raise NotImplementedError("{} is not a standalone object; purpose = inheritance.".format(type(self).__name__))
