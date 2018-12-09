import numpy as np


class _BasePropagator(object):
    def __init__(self, x0, eom):
        self._eom = eom
        self._x0 = x0


class TranslationalPropagator(_BasePropagator):
    def __init__(self, x0, eom, t_array):
        super().__init__(x0, eom)
