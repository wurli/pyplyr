import numpy as np

def _as_id(x: np.ndarray, axis=0):
    _, id = np.unique(x, return_inverse=True, axis=axis)
    return id

def _reorder(l, items, after = None):

    after = -1 if after is None else after % len(l)

    start = []
    middle = []
    end = []
    for i, x in enumerate(l):
        if x in items:
            middle.append(x)
        elif i <= after:
            start.append(x)
        else:
            end.append(x)
    return start + middle + end


