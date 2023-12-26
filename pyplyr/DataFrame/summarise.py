from .._utils import _make_col

def summarise(self, **kwargs):
    by = kwargs.pop('_by', None)
    return self.copy()._by_group(by, lambda g: _summarise_group(g, **kwargs))


def _summarise_group(g, **kwargs):
    for colname, x in kwargs.items():
        g[colname] = _make_col(g, x)
    return g
