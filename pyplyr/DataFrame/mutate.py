from .._utils import _make_col

def mutate(self, **kwargs):
    by = kwargs.pop('_by', None)
    return self.copy()._by_group(by, lambda g: _mutate_group(g, **kwargs))


def _mutate_group(g, **kwargs):
    for colname, x in kwargs.items():
        g[colname] = _make_col(g, x)
    return g
