def __repr__(self):
    header  = f"A DataFrame: {self.nrow()} x {self.ncol()}"
    rownums = _as_pillar('', np.array(range(self.nrow())), show_type=False)
    pillars = [_as_pillar(name, val) for name, val in self.data.items()]
    body    = "\n".join([" ".join(row) for row in zip(rownums, *pillars)])
    return f"{header}\n{body}"

def _as_pillar(colname, colval, show_type=True):
    coltype = f"<{colval.dtype.name}>"
    pillar = [colname, coltype if show_type else ''] + list(colval.astype(str))
    max_len = max([len(s) for s in pillar])

    justify_right = any([t in coltype for t in ['int', 'float']])

    return [
        s.rjust(max_len) if justify_right else s.ljust(max_len)
        for s in pillar
    ]