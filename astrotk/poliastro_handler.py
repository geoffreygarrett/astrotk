""" poliastro_handler.py
"""

# Authorship ----------------------------------------------------------------------------------------------------------#
__author__      = "Geoffrey Hyde Garrett"
__copyright__   = None
__credits__     = None
__license__     = "MIT"
__version__     = "1.0.0"
__maintainer__  = "Geoffrey Hyde Garrett"
__email__       = "g.h.garrett13@gmail.com"
__status__      = "Pre-alpha"

# Imports -------------------------------------------------------------------------------------------------------------#
from astropy.coordinates import solar_system_ephemeris
from astropy.coordinates import get_body_barycentric_posvel
solar_system_ephemeris.set('jpl')


# Functions -----------------------------------------------------------------------------------------------------------#
def body_2_mu(body) -> float:  # km^3/s^2
    """
    :param body:
    :return: <float> (km^3/ m^2)
    """
    return body.k.to('u.km^3/u.s^2').value


def body_2_barycentric_posvel(body, time, ephemeris=None) -> tuple:
    """

    :param body:
    :param time:
    :param ephemeris:
    :return:
    """
    return get_body_barycentric_posvel(body, time, ephemeris=ephemeris)

