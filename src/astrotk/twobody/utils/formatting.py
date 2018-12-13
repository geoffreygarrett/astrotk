from copy import deepcopy
# from astrotk.twobody.utils import
from math import floor, log10

import astropy.units as u
import numpy as np
import pandas as pd
from prettytable import PrettyTable

dict_latex = {
    '_a': "$a$",
    '_e': "$e$",
    '_inc': "$i$",
    '_raan': "$\Omega{}$",
    '_argp': "$\omega{}$",
    '_theta': "$\\theta{}$",
    '_ra': "$\\alpha{}$",
    '_de': "$\delta{}$",
    '_fpa': "$\gamma{}$",
    '_v': "$V$",
    '_r_vec': "$\mathbf{r}$",
    '_v_vec': "$\mathbf{V}$",
    '_attractor': "Focus",
}
dict_quantity = {
    'rad': "deg"
}


# TODO: Resolve DeprecationWarning: invalid escape sequence for above mapper.


def _prettytable_map(dict):
    t = PrettyTable(['element', 'value', 'unit'])
    for key, val in dict.items():
        if val.unit is u.rad:
            t.add_row([key.replace('_', ''), val.to(u.deg).value, val.to(u.deg).unit])
        else:
            t.add_row([key.replace('_', ''), val.value, val.unit])
    return t


def prettytable_state(state):
    _temp = deepcopy(state.__dict__)
    _temp.pop('_attractor')
    _keys = list(_temp.keys())
    _dict = dict([(k, v) for k, v in zip(_keys, [_temp[_keys[i]] for i in range(len(_keys))])])
    _t = _prettytable_map(_dict)
    return _t


def sig_fig(value: float, sf: int) -> float:
    """Round to specified number of sigfigs.

    >>> sig_fig(0, sf=4)
    0
    >>> int(sig_fig(12345, sf=2))
    12000
    >>> int(sig_fig(-12345, sf=2))
    -12000
    >>> int(sig_fig(1, sf=2))
    1
    >>> '{0:.3}'.format(sig_fig(3.1415, sf=2))
    '3.1'
    >>> '{0:.3}'.format(sig_fig(-3.1415, sf=2))
    '-3.1'
    >>> '{0:.5}'.format(sig_fig(0.00098765, sf=2))
    '0.00099'
    >>> '{0:.6}'.format(sig_fig(0.00098765, sf=3))
    '0.000988'
    """
    if value != 0:
        return round(value, -int(floor(log10(abs(value))) - (sf - 1)))
    else:
        return 0  # Can't take the log of 0


def latex(state, sf=10):
    if type(state).__name__ is "VectorState":
        data = {"$r_x$": state.r_vec[0],
                "$r_y$": state.r_vec[1],
                "$r_z$": state.r_vec[2],
                "$V_x$": state.v_vec[0],
                "$V_y$": state.v_vec[1],
                "$V_z$": state.v_vec[2]}
        df = pd.DataFrame.from_dict(data, orient='index', columns=['value']).reset_index()
        df = df.rename(index=str, columns={"index": "element"})
    else:
        df = pd.DataFrame.from_dict(vars(state), orient='index', columns=['value']).reset_index()
        df = df.rename(index=str, columns={"index": "element"})
        df = df.iloc[1:]
    df.value = df.value.apply(lambda x: x.si.value * x.si.unit)
    df.value = df.value.apply(lambda x: x.to(dict_quantity[str(x.si.unit)]) if str(x.si.unit) in
                                                                               set(dict_quantity.keys()) else x)
    df.value = df.value.apply(lambda x: sig_fig(x.value, sf) * x.unit)
    df.element = df.element.apply(lambda x: dict_latex[x] if x in set(dict_latex.keys()) else x)
    return df.to_latex(escape=False, index=False)


def positive_angle(angle_rad):
    return angle_rad + 2 * np.pi if angle_rad <= 0 else angle_rad
