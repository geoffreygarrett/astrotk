from prettytable import PrettyTable
import astropy.units as u
from copy import deepcopy
import sympy
from sympy import latex
import pandas as pd

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
    before, after = str(value).split('.')
    n_b, n_a = len(before), len(after)
    if sf < n_b:
        return int(((int(before[:sf]) + 1) * eval('1E{}'.format(n_b - sf)) if int(before[sf]) >= 5 else
                  (int(before[:sf])) * eval('1E{}'.format(n_b - sf))))

    elif sf == n_b:
        return int(before) + 1 if int(after[0]) >= 5 else int(before)

    elif sf > n_b:
        n_d = sf - n_b +1
        try:
            return (float("0."+str(int(after[:n_d]) + 1)) if int(after[n_d+1]) >= 5 else
                    float("0."+str(int(after[:n_d]))))
        except IndexError:
            return float("0." + str(int(after[:n_d])))


def latex(state, sf=10):
    df = pd.DataFrame.from_dict(vars(state), orient='index', columns=['value']).reset_index()
    df = df.rename(index=str, columns={"index":"element"})
    df = df.iloc[1:]
    print(df)
    df.value = df.value.apply(lambda x: u.Quantity.round(x, 10))
    df.element = df.element.apply(lambda x: dict_latex[x])
    print(df.to_latex(escape=False, index=False))
    # df.value = df[0].apply(lambda x: )
    return df


# if __name__ == "__main__":


