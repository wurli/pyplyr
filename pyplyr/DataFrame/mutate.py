def mutate(self, _by = None, **kwargs):
    return self.copy()._by_group(_by, lambda g: _mutate_group(g, **kwargs))


def _mutate_group(g, **kwargs):
    for colname, x in kwargs.items():
        if callable(x):
            x = _mutate_lambda(g, x)
        g[colname] = x
    return g


def _mutate_lambda(g, f):

    input_cols = list(f.__code__.co_varnames)
    existing_cols = g.colnames()

    bad_args = [col for col in input_cols if col not in existing_cols]
    if len(bad_args) > 0:
        bad_args = ", ".join(bad_args)
        raise ValueError(f"Bad input: non-existent column(s) `{bad_args}`")
    
    return f(**g[input_cols])