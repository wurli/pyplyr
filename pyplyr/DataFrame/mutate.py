def mutate(self, **kwargs):
    for colname, x in kwargs.items():
        if callable(x):
            x = _mutate_lambda(self, x)
        self[colname] = x
    return self


def _mutate_lambda(df, f):
    args = list(f.__code__.co_varnames)
    cols = df.colnames()

    bad_args = [arg for arg in args if arg not in cols]
    if len(bad_args) > 0:
        bad_args = ", ".join(bad_args)
        raise ValueError(f"Bad input: non-existent column(s) `{bad_args}`")

    return f(**{col: df[col] for col in args})