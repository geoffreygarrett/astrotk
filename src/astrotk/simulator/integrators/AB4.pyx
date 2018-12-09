def step(x0, f, h=1., t0=0.):
    st = 1./24.*(-9. * f(t0-3. * h, x0))
    return x0 + h * st

def integrate(x0, f, t1, h=1., t0=0.):
    t = t0
    _x0 = x0
    while t <= t1:
        x1 = step(_x0, f, h, t0)
        _x0 = x1
        t += h
    return x1


def integrate2(x0, f, t):
    sol = [x0]
    for idx in range(len(t) - 1):
        _t0 = t[idx]
        sol.append(step(sol[idx], f,
                        h=t[idx + 1] - _t0,
                        t0=_t0))
    return sol
