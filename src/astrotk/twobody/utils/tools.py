
def rounding_precision(expected):
    return eval('10E-{}'.format(len(str(expected).split('.')[1]) + 1))
