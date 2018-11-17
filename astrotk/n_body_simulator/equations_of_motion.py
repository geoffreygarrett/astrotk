""" equations_of_motion.py
"""

# Authorship ----------------------------------------------------------------------------------------------------------#
__author__ = "Geoffrey Hyde Garrett"
__copyright__ = None
__credits__ = None
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Geoffrey Hyde Garrett"
__email__ = "g.h.garrett13@gmail.com"
__status__ = "Pre-alpha"

# Imports -------------------------------------------------------------------------------------------------------------#
import numpy as np
G = 6.67408 * 10 ** (-3)


def scalar_barycentric_acceleration(mu_list, i, r):
    j_not_i = list(range(len(mu_list))[:i]) + list(range(len(mu_list)))[i + 1:]
    return  - sum(mu_list) / (np.linalg.norm(r[i]) ** 3) * r[i] \
            + np.sum([mu_list[j] * ((1/(np.linalg.norm(-r[j]+r[i]) ** 3)) - 1/(np.linalg.norm(r[i])**3)) * (r[j]-r[i]) for j in j_not_i], axis=1)


def scalar_fixed_acceleration(r, mu_list, i):
    j_not_i = list(range(len(mu_list))[:i]) + list(range(len(mu_list)))[i + 1:]


def adjust_for_cm(r, mu_List):
    return r + np.sum(np.multiply(np.array(mu_List), r)) / sum(mu_List)


# Barycentric
def vector_barycentric_acceleration(Y: np.ndarray, mu_list: list):
    pos, vel = np.split(Y, 2)
    print(Y)
    pos_x_0 = pos[0::3]
    pos_y_0 = pos[1::3]
    pos_z_0 = pos[2::3]

    vel_x_0 = vel[0::3]
    vel_y_0 = vel[1::3]
    vel_z_0 = vel[2::3]

    acc_x_0 = []
    acc_y_0 = []
    acc_z_0 = []

    # r = np.sqrt(np.square(pos_x_0) + np.square(pos_y_0) + np.square(pos_z_0))

    r = np.concatenate(([pos_x_0], [pos_y_0], [pos_z_0])).T
    r_cm = np.sum([r[i] * mu_list[i] for i in range(len(mu_list))], axis=0) / np.sum(np.array(mu_list))
    r = r + r_cm

    for i in range(len(mu_list)):
        print(i, scalar_barycentric_acceleration(mu_list, i, r))
        acc_x_i, acc_y_i, acc_z_i = scalar_barycentric_acceleration(mu_list, i, r)
        acc_x_0.append(acc_x_i)
        acc_y_0.append(acc_y_i)
        acc_z_0.append(acc_z_i)

    return np.array([[vx, vy, vz, ax, ay, az] for vx, vy, vz, ax, ay, az in zip(
        vel_x_0,
        vel_y_0,
        vel_z_0,
        acc_x_0,
        acc_y_0,
        acc_z_0
    )]).flatten()


# Barycentric
def vector_fixed_acceleration(Y: np.ndarray, mu_list: list):
    pos, vel = np.split(Y, 2)
    pos_x_0 = pos[0::3]
    pos_y_0 = pos[1::3]
    pos_z_0 = pos[2::3]
    vel_x_0 = vel[0::3]
    vel_y_0 = vel[1::3]
    vel_z_0 = vel[2::3]

    acc_x_0 = []
    acc_y_0 = []
    acc_z_0 = []
    for i in range(len(mu_list)):
        acc_x_i = scalar_fixed_acceleration(pos_x_0, mu_list, i)
        acc_y_i = scalar_fixed_acceleration(pos_y_0, mu_list, i)
        acc_z_i = scalar_fixed_acceleration(pos_z_0, mu_list, i)
        acc_x_0.append(acc_x_i)
        acc_y_0.append(acc_y_i)
        acc_z_0.append(acc_z_i)

    return np.array([[vx, vy, vz, ax, ay, az] for vx, vy, vz, ax, ay, az in zip(
        vel_x_0,
        vel_y_0,
        vel_z_0,
        acc_x_0,
        acc_y_0,
        acc_z_0
    )]).flatten()


# Functions -----------------------------------------------------------------------------------------------------------#


# if __name__ == "__main__":


# print(Earth.k.to('u.km^3/u.s^2').value)
