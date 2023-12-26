import numpy as np

def arrange(self, *args, **kwargs):
    sort_cols = list(args)
    new_order = np.lexsort(
        list(reversed(self[sort_cols].values())),
        axis=0
    )
    return self[new_order, None]
