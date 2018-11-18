

import collections
import numpy as np
from astrotk_dev.poliastro_handler import *
from astrotk.nbody.simulator.equations_of_motion import vector_barycentric_acceleration

# For initial conditions



# def step(bodies.py):
#     a = eom_barycentric(bodies.py)
#     for body in bodies.py:


class NBodySystem(object):

    @staticmethod
    def convert_poliastro_bodies(body_list, time):
        new_list=[]
        Body = collections.namedtuple('Body', ['mu', 'pos', 'vel'])
        for body in body_list:
            r, v = body_2_barycentric_posvel(body, time=time)
            new_list.append(Body(mu=body_2_mu(body), pos=r, vel=v))
        return new_list

    def __init__(self, bodies, time=None):
        if time:
            self._time=time
        else:
            self._time=None

        # List or path to config file
        if type(bodies) is list:
            self._bodies = bodies

        elif type(bodies) is str:
            # Import configuration file
            # TODO: Add configuration file import
            raise NotImplementedError("TODO: Add configuration file import")
        else:
            raise SystemError("Argument <{}> not recognised for bodies.py".format(bodies))

        # Poliastro body object or custom body object
        if hasattr(bodies[0], 'k'):
            self._bodies = self.convert_poliastro_bodies(self._bodies, time)

        self._mu_list = [body.mu for body in self._bodies]
        print(self._mu_list)

        self._y = self._initial_y()

    def __getitem__(self, item):
        return self._bodies[item]

    def _initial_y(self):
        y = self._bodies[0].pos
        for body in self._bodies[1:]:
            y = np.vstack((y, body.pos))
        for body in self._bodies:
            y = np.vstack((y, body.vel))
        return y.flatten()

    def _dy(self):
        return vector_barycentric_acceleration(self._y, self._mu_list)

    def step(self, integrator, dt):
        self._y -= integrator(self._y, self._dy(), dt)




    # def step(self):
    #     self._bodies, previous_a_v_p = step(self._bodies)
    #     self._record_state(previous_a_v_p)

# if __name__=="__main__":
