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


def _make_col(dfs, x):
    if not callable(x):
        return x

    input_cols = list(x.__code__.co_varnames)
    existing_cols = {c for df in dfs for c in df.colnames()}

    bad_args = [col for col in input_cols if col not in existing_cols]
    if len(bad_args) > 0:
        bad_args = ", ".join(bad_args)
        raise ValueError(f"Bad input: non-existent column(s) `{bad_args}`")
    
    def get_col(c):
        for df in dfs:
            if c in df.colnames():
                return df[c]
    
    return x(**{c: get_col(c) for c in input_cols})


def _to_vector(x):
    """Convert a scalar to a vector, or leave a vector unchanged."""
    scalars = [str, int, float, bool, type(None)]
    vectors = [list, np.ndarray]
    if any([isinstance(x, t) for t in scalars]):
        return [x]
    if any([isinstance(x, t) for t in vectors]):
        return x
    raise TypeError(f'Cannot convert {type(x)} to vector')
    