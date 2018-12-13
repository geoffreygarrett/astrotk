from astrotk.simulator.integrators.INTEG.common import *

args_car = {
    "step_size": 1.,
    "duration": 60.,
    "t": np.arange(0., 60., 1.),
    "y0": np.array([0.0, 0.0]),
    "eom": cy_racing_car,
    "args": 2.0,
    "x": 0,
    "dx": 1,
    "plot": {
    },
}

# GENERAL PLOT
# plt.ylabel("Distance [m]")
# plt.rcParams.update(args_plot)
# plt.subplot(2, 1, 1)
# plot(args_car, args_plot, propagate(Euler, args_car, 0.1))
# plt.ylabel("Position [m]")
# plt.subplot(2, 1, 2)
# plot(args_car, args_plot, propagate(Euler, args_car, 0.1), type="t_dx")
# plt.xlabel("Time [s]")
# plt.ylabel("Velocity [m/s]")
# plt.savefig("one.png")
# plt.show()

# FINAL SOLUTION
print(final_solution(Euler, args_car, 0.1))

# RANGE OF STEP SIZES
step_size_array_car = np.logspace(-3, 2, 200)

# RUNGE-KUTTA 4 ERROR FOR INTEG 1
# error_car_RK = [
#     abs(propagate(RK4, args_car, ts)[-1][0] - 3600.)
#     for ts in step_size_array_car
# ]

# EULER ERROR FOR INTEG 1
error_car_EULER = np.array([
    np.abs(propagate(RK4, args_car, ts)[-1] - np.array([3600., 120.]))
    for ts in step_size_array_car
])

# error_car_EULER = [
#     abs(propagate(Euler, args_car, ts)[-1][1] - 120.)
#     for ts in step_size_array_car
# ]
#
# # NUMBER OF EVALUATIONS
# qty_evaluations = 60. / step_size_array_car
# qty_car_EULER = qty_evaluations
# qty_car_RK4 = qty_evaluations * 4

# TIME TAKEN (COMPUTATIONAL)
# time_car_RK4 = [
#     time_it(propagate, (RK4, args_car, ts))
#     for ts in step_size_array_car
# ]
#
# time_car_Euler = [
#     time_it(propagate, (Euler, args_car, ts))
#     for ts in step_size_array_car
# ]

# ERROR PLOT
plt.rcParams.update(args_plot)
plt.grid(True, which="both")
plt.ylabel("Error ($\epsilon$) [m]")
plt.xlabel("Step size ($\delta{s}$) [s]")
plt.loglog(step_size_array_car, error_car_EULER[:, 0], label="Position")
plt.loglog(step_size_array_car, error_car_EULER[:, 1], label="Velocity")
plt.legend()
plt.savefig("INTEG1_RK4_error_ds_e.png")
plt.show()
print(np.sum(error_car_EULER[:, 1]))
# plt.savefig("INTEG_RK4_error_ds_e.png")

# TIME PLOT
# plt.rcParams.update(args_plot)
# plt.loglog(step_size_array_car, time_car_Euler, label="Euler")
# plt.loglog(step_size_array_car, time_car_RK4, label="RK4")
# plt.legend()
# plt.ylabel("Computational Time [s]")
# plt.xlabel("Step size ($\delta{s}$) [s]")
# plt.savefig("INTEG1_time.png")
# plt.show()

# EVAL PLOT
# plt.rcParams.update(args_plot)
# plt.grid(True, which="both")
# plt.xlabel("Error ($\epsilon$) [m]")
# plt.ylabel("# of derivative evaluations [-]")
# plt.loglog(error_car_EULER, qty_car_EULER, label="Euler")
# plt.loglog(error_car_RK, qty_car_RK4, label="RK4")
# plt.legend()
# plt.savefig("INTEG1_error_vs_qty.png")
# plt.show()


# propagate(Euler)
