from prettytable import PrettyTable
import astropy.units as u
from copy import deepcopy
import sympy
from sympy import latex
import pandas as pd
import numpy as np
# from astrotk.twobody.utils import

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
    _temp.pop('_orbital_expressions')
    _temp.pop('_attractor')
    _keys = list(_temp.keys())
    _dict = dict([(k, v) for k, v in zip(_keys, [_temp[_keys[i]] for i in range(len(_keys))])])
    _t = _prettytable_map(_dict)
    return _t


def sig_fig(value: float, sf: int) -> float:
    # TODO: sig_fig(1.2345, 1) returns 1.0. Should be 1
    rounded_str = str(float('%s' % float('%.{}g'.format(sf) % value)))
    if '-' in rounded_str:
        addon = 2
    else:
        addon = 1
    if ('.' in rounded_str) and (len(rounded_str) != sf + addon):
        rounded_str = rounded_str + '0' * (sf - len(rounded_str) + addon)
    return float(rounded_str)


def latex(state, sf=10):
    df = pd.DataFrame.from_dict(vars(state), orient='index', columns=['value']).reset_index()
    df = df.rename(index=str, columns={"index": "element"})
    df = df.iloc[1:]
    df.value = df.value.apply(lambda x: x.to(dict_quantity[str(x.si.unit)]) if str(x.si.unit) in
                                                                               set(dict_quantity.keys()) else x)
    df.value = df.value.apply(lambda x: sig_fig(x.value, sf) * x.unit)
    df.element = df.element.apply(lambda x: dict_latex[x])
    return df.to_latex(escape=False, index=False)


def positive_angle(angle_rad):
    return angle_rad + 2 * np.pi if angle_rad <= 0 else angle_rad
