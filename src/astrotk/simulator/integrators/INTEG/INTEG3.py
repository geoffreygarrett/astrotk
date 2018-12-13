from astrotk.bodies.bodies import Earth
from astrotk.simulator.integrators.INTEG.common import *
from astrotk.twobody.utils.transformation import vector2classical

D = 86164.1004  # s
mu = 398600.441 * u.km ** 3 / u.s / u.s
a = ((D / (2 * np.pi)) ** 2 * mu.si.value) ** (1. / 3.) * u.m
v = np.sqrt(mu / a)
ds = 1400.
de = 30 * 24 * 3600.
print(2 * np.pi * (a.si.value ** 3 / mu.si.value) ** (1 / 2.))

# args_plot = {
#     "figure.dpi": 300,
#     "figure.figsize": (6.3, 5.3),
#     "axes.grid": True,
#     "grid.color": "#00A6D6",
#     "grid.linewidth": 0.8,
# }


# BASE ARGUMENTS
args_sat = {
    "step_size": ds,
    "duration": de,
    "y0": np.array([a.si.value, 0, 0, v.si.value]),
    "eom": cy_point_mass_acceleration,
    "args": mu.si.value,
    "x": 0,
    "y": 1,
    "dx": 2,
    "dy": 3,
    "plot": {
        "image.aspect": "equal"
    }
}


def error_radial_Euler():
    step_size_array_sat = np.logspace(2, 4, 100)
    error_sat_EULER = [
        abs(np.linalg.norm(propagate(Euler, args_sat, ts)[-1][0:2]) - a.si.value)
        for ts in step_size_array_sat
    ]
    # ERROR PLOT
    plt.rcParams.update(args_plot)
    plt.minorticks_on()
    plt.grid(True, which="both")
    plt.ylabel("Error ($\epsilon$) [m]")
    plt.xlabel("Step size ($\delta{s}$) [s]")
    plt.loglog(step_size_array_sat, error_sat_EULER)
    plt.savefig("INTEG3_EULER_error_ds_e.png")
    plt.show()


def error_radial_RK():
    step_size_array_sat = np.logspace(2, 4, 100)
    error_sat_RK = [
        abs(np.linalg.norm(propagate(RK4, args_sat, ts)[-1][0:2]) - a.si.value)
        for ts in step_size_array_sat
    ]
    # ERROR PLOT
    plt.rcParams.update(args_plot)
    plt.minorticks_on()
    plt.axes().yaxis.set_tick_params(which='minor', left='on')
    plt.grid(True, which="both")
    plt.ylabel("Error ($\epsilon$) [m]")
    plt.xlabel("Step size ($\delta{s}$) [s]")
    plt.loglog(step_size_array_sat, error_sat_RK)
    plt.savefig("INTEG3_RK4_error_ds_e.png")
    plt.show()


def time_comparison():
    step_size_array_sat = np.logspace(2, 4, 100)
    time_sat_Euler = [
        time_it(propagate, (Euler, args_sat, ts))
        for ts in step_size_array_sat
    ]
    time_sat_RK4 = [
        time_it(propagate, (RK4, args_sat, ts))
        for ts in step_size_array_sat
    ]
    # TIME PLOT
    plt.rcParams.update(args_plot)
    plt.grid(True, which="both")
    plt.loglog(step_size_array_sat, time_sat_Euler, label="Euler")
    plt.loglog(step_size_array_sat, time_sat_RK4, label="RK4")
    plt.legend()
    plt.ylabel("Computational Time [s]")
    plt.xlabel("Step size ($\delta{s}$) [s]")
    plt.savefig("INTEG3_time.png")
    plt.show()


def eval_comparison():
    step_size_array_sat = np.logspace(2, 4, 100)
    error_sat_EULER = [
        abs(np.linalg.norm(propagate(Euler, args_sat, ts)[-1][0:2]) - a.si.value)
        for ts in step_size_array_sat
    ]
    error_sat_RK = [
        abs(np.linalg.norm(propagate(RK4, args_sat, ts)[-1][0:2]) - a.si.value)
        for ts in step_size_array_sat
    ]
    # # NUMBER OF EVALUATIONS
    qty_evaluations = de / step_size_array_sat
    qty_sat_EULER = qty_evaluations
    qty_sat_RK4 = qty_evaluations * 4
    # EVAL PLOT
    plt.rcParams.update(args_plot)
    plt.grid(True, which="both")
    plt.xlabel("Error ($\epsilon$) [m]")
    plt.ylabel("# of derivative evaluations [-]")
    plt.loglog(error_sat_EULER, qty_sat_EULER, label="Euler")
    plt.loglog(error_sat_RK, qty_sat_RK4, label="RK4")
    plt.legend()
    plt.savefig("INTEG3_error_vs_qty.png")
    plt.show()


def cart2kep(state, attractor):
    return vector2classical(np.append(state[0:2], 0), np.append(state[2:4], 0), attractor.mu.si.value)


def pre_cart2kep(state):
    return cart2kep(state, Earth)


def sol2kep(sol):
    return pre_cart2kep(sol)


def general_solution_kep():
    sat_t_array = np.arange(0, de, ds)
    cart_sol = propagate(Euler, args=args_sat, ts=100.)
    kep_sol = np.apply_along_axis(sol2kep, 1, cart_sol)

    plt.subplot(2, 1, 1)
    plt.minorticks_on()
    plt.grid(True, which="major", linewidth=1.0)
    plt.grid(True, which="minor", linewidth=0.3)
    plt.ylabel("Semi-major axis error (|a|) [m]")
    plt.plot(sat_t_array / 3600, kep_sol[:, 0][:-1])
    plt.subplot(2, 1, 2)
    plt.minorticks_on()
    plt.ylabel("Eccentricity error (|e|) [-]")
    plt.xlabel("Time propagated [s]")
    plt.grid(True, which="major", linewidth=1.0)
    plt.grid(True, which="minor", linewidth=0.3)
    plt.plot(sat_t_array / 3600, kep_sol[:, 1][:-1])
    plt.show()

    cart_sol = propagate(RK4, args=args_sat, ts=100.)
    kep_sol = np.apply_along_axis(sol2kep, 1, cart_sol)

    plt.subplot(2, 1, 1)
    plt.minorticks_on()
    plt.grid(True, which="major", linewidth=1.0)
    plt.grid(True, which="minor", linewidth=0.3)
    plt.ylabel("Semi-major axis error (|a|) [m]")
    plt.plot(sat_t_array / 3600, kep_sol[:, 0][:-1])
    plt.subplot(2, 1, 2)
    plt.minorticks_on()
    plt.ylabel("Eccentricity error (|e|) [-]")
    plt.xlabel("Time propagated [s]")
    plt.grid(True, which="major", linewidth=1.0)
    plt.grid(True, which="minor", linewidth=0.3)
    plt.plot(sat_t_array / 3600, kep_sol[:, 1][:-1])
    plt.show()


def kep_error_analysis(integrator):
    step_size_array_sat = np.logspace(2, 4, 100)
    list_a = []
    list_e = []
    for stepsize in step_size_array_sat:
        print("stepsize: ", stepsize)
        cart_sol = propagate(integrator, args=args_sat, ts=stepsize)
        kep_sol = np.apply_along_axis(sol2kep, 1, cart_sol)[-1]
        _a, _e, _, _, _, _ = kep_sol
        list_a.append(_a)
        list_e.append(_e)

    error_a = np.array(list_a) - a.si.value
    error_e = np.array(list_e)

    return error_a, error_e


def kep_error_Euler():
    step_size_array_sat = np.logspace(2, 4, 100)
    err_a, err_e = kep_error_analysis(Euler)

    plt.rcParams.update(args_plot)
    plt.subplot(2, 1, 1)
    plt.minorticks_on()
    plt.ylabel("Semi-major axis error (|$\epsilon_a$|) [m]")
    # plt.xlabel("Step size ($\delta{s}$) [s]")
    plt.grid(True, which="major", linewidth=1.0)
    plt.grid(True, which="minor", linewidth=0.3)
    plt.loglog(step_size_array_sat, abs(err_a))

    plt.subplot(2, 1, 2)
    # plt.rcParams.update(args_plot)
    plt.minorticks_on()
    plt.ylabel("Eccentricity error (|$\epsilon_e$|) [-]")
    plt.xlabel("Step size ($\delta{s}$) [s]")
    plt.grid(True, which="major", linewidth=1.0)
    plt.grid(True, which="minor", linewidth=0.3)
    plt.loglog(step_size_array_sat, err_e)
    plt.savefig("INTEG3_error_over_time_EULER.png")
    plt.show()


def kep_error_RK4():
    step_size_array_sat = np.logspace(2, 4, 100)
    err_a, err_e = kep_error_analysis(RK4)

    plt.rcParams.update(args_plot)
    plt.axes().yaxis.set_tick_params(which='minor', left='on')
    plt.subplot(2, 1, 1)
    plt.minorticks_on()
    plt.ylabel("Semi-major axis error (|$\epsilon_a$|) [m]")
    # plt.xlabel("Step size ($\delta{s}$) [s]")
    plt.grid(True, which="major", linewidth=1.0)
    plt.grid(True, which="minor", linewidth=0.3)
    plt.loglog(step_size_array_sat, abs(err_a))

    plt.axes().yaxis.set_tick_params(which='minor', left='on')
    plt.subplot(2, 1, 2)
    # plt.rcParams.update(args_plot)
    plt.minorticks_on()
    plt.ylabel("Eccentricity error (|$\epsilon_e$|) [-]")
    plt.xlabel("Step size ($\delta{s}$) [s]")
    plt.grid(True, which="major", linewidth=1.0)
    plt.grid(True, which="minor", linewidth=0.3)
    plt.loglog(step_size_array_sat, err_e)
    plt.savefig("INTEG3_error_over_time_RK4.png")
    plt.show()


def plot_cartesian(sol):
    plt.rcParams.update(args_plot)
    plt.axes().set_aspect('equal', 'datalim')
    plt.ylabel("y-coordinate [m]")
    plt.xlabel("x-coordinate [m]")
    plt.minorticks_on()
    plt.grid(True, which="major", linewidth=1.0)
    plt.grid(True, which="minor", linewidth=0.3)
    plt.plot(sol[:, 0][0:int(D / 4000) + 1], sol[:, 1][0:int(D / 4000) + 1], label="First orbit")
    plt.plot(sol[:, 0][-int(D / 4000) - 1:-1], sol[:, 1][-int(D / 4000) - 1:-1], label="Last orbit")
    plt.legend()
    plt.savefig('INTEG3_cart.png')
    plt.show()


if __name__ == "__main__":
    # kep_error_Euler()
    # kep_error_RK4()
    # error_radial_Euler()
    # error_radial_RK()

    # plot_cartesian(propagate(RK4, args_sat, 4000.))

    eval_comparison()
    time_comparison()
