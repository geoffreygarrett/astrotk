from prettytable import PrettyTable
import astropy.units as u
from copy import deepcopy

dict_latex = {
    '_a': "$a$",
    '_e': "$e$",
    '_inc': "$i$",
    '_raan': "$/Omega{}$",
    '_argp': "$/omega{}$",
    '_theta': "$/theta{}$"
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
