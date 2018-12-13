import astropy.units as u

from astrotk.bodies.constants import *

# Redefining the definition of AU from 149597870.7 to 149597870.66 for course AE4878 verification.
u.AU = u.def_unit('AU', course_constants["AU"]["val"] * eval(course_constants["AU"]["unit"]))


# Standard BaseClass structure for a point mass modeled gravitational model in the two-body problem.
class _Body(object):
    def __init__(self, mu, R, parent_body=None):
        self._mu = mu
        self._R = R
        self._parent_body = parent_body

    def __str__(self):
        return type(self).__name__

    @property
    def mu(self):
        """
        :return: <astropy.units> The value of mu for the body.
        """
        return self._mu

    @property
    def R(self):
        """
        :return: <astropy.units> The value of R (average radius) for the body.
        """
        return self._R

    @property
    def parent(self):
        """
        :return: <astropy.units> Returns the main attracting body (Occupied foci in the two-body problem).
        """
        return self._parent_body


class Sun(_Body):
    def __init__(self):
        _Body.__init__(self,
                       mu=course_constants["muSun"]["val"] * eval(course_constants["muSun"]["unit"]),
                       R=course_constants["RSun"]["val"] * eval(course_constants["RSun"]["unit"]),
                       parent_body=None
                       )


class Earth(_Body):
    def __init__(self):
        _Body.__init__(self,
                       mu=course_constants["muEarth"]["val"] * eval(course_constants["muEarth"]["unit"]),
                       R=course_constants["RE"]["val"] * eval(course_constants["RE"]["unit"]),
                       parent_body=Sun
                       )


class Mars(_Body):
    def __init__(self):
        _Body.__init__(self,
                       mu=course_constants["muMars"]["val"] * eval(course_constants["muMars"]["unit"]),
                       R=course_constants["RMars"]["val"] * eval(course_constants["RMars"]["unit"]),
                       parent_body=Sun
                       )


class Jupiter(_Body):
    def __init__(self):
        _Body.__init__(self,
                       mu=course_constants["muJupiter"]["val"] * eval(course_constants["muJupiter"]["unit"]),
                       R=course_constants["RJupiter"]["val"] * eval(course_constants["RJupiter"]["unit"]),
                       parent_body=Sun
                       )


Jupiter = Jupiter()
Mars = Mars()
Sun = Sun()
Earth = Earth()
