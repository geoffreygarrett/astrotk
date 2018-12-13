import time

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams.update(mpl.rcParamsDefault)

args_plot = {
    "figure.dpi": 300,
    "figure.figsize": (6.0, 5.5),
    "axes.grid": True,
    # "grid.color": "#00A6D6",
    "grid.linewidth": 0.8,
}


def propagate(integrator, args, ts):
    args.update(
        {
            "t": np.array(list(np.arange(0., args["duration"], ts)) + [args["duration"]]),
        }
    )
    return integrator.odeint(args["eom"], args["y0"], args["t"], args=args["args"])


def propagate2(integrator, args):
    return integrator.odeint(args["eom"], args["y0"], args["t"], args=args["args"])


def plot(eom_args, plot_args, sol, type="t_x"):
    plot_args.update(eom_args["plot"])
    plt.rcParams.update(plot_args)
    _x, _y = type.split("_")
    if _x is "t":
        X = eom_args["t"]
    elif _x in set(["x", "y", "dx", "dy"]):
        X = sol[:, eom_args[_x]]
    if _y is "t":
        Y = eom_args["t"]
    elif _y in set(["x", "y", "dx", "dy"]):
        Y = sol[:, eom_args[_y]]
    plt.plot(X, Y)
    plt.grid(which="minor", color="grey", linewidth="0.2")
    plt.minorticks_on()


def final_solution(integrator, args, time_step):
    args.update({"time_step": time_step})
    return propagate(integrator, args, time_step)[-1]


def time_it(func, args):
    now = time.time()
    func(*args)
    return (time.time() - now)
