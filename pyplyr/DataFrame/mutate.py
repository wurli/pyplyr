from .._utils import _make_col

def mutate(self, _by=None, **kwargs):
    return self.copy()._by_group(_by, lambda g: _mutate_group(g, **kwargs))


def _mutate_group(g, **kwargs):
    for colname, x in kwargs.items():
        g[colname] = _make_col(g, x)
    return g
