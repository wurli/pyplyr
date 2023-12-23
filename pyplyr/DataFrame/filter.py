import numpy as np
from .._utils import _make_col

def filter(self, *args, **kwargs):
    by = kwargs.pop('_by', None)
    return self.copy()._by_group(by, lambda g: _filter_group(g, *args))

def _filter_group(g, *args):
    filters = [_make_col(g, x) for x in args]
    overall_filter = np.all(filters, axis=0)

    return g[overall_filter, None]

