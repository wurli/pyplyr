from .._utils import _make_col, _to_vector

def summarise(self, **kwargs):
    by = kwargs.pop('_by', None)
    return self.copy()._by_group(by, lambda g: _summarise_group(g, kwargs, by))


def _summarise_group(g, fns, by):
    summarised = g[[0], _to_vector(by)]
    for colname, x in fns.items():
        summarised[colname] = _make_col([summarised, g], x)
    return summarised
