import numpy as np

def arrange(self, *args, **kwargs):
    by = kwargs.pop('_by', None)
    return self.copy()._by_group(by, lambda g: _arrange_group(g, *args))

def _arrange_group(g, *args):
    sort_cols = list(args)
    new_order = np.lexsort(
        list(reversed(g[sort_cols].values())),
        axis=0
    )
    return g[new_order, None]
