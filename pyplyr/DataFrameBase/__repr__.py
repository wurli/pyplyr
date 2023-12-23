import numpy as np

def __repr__(self):
    header  = f"# A DataFrame: {self.nrow()} x {self.ncol()}"
    rownums = _as_pillar('', np.array(range(self.nrow() + 1)), show_type=False)
    pillars = [_as_pillar(name, val) for name, val in self.items()]
    body    = "\n".join([" ".join(row) for row in zip(rownums, *pillars)])
    return f"{header}\n{body}\n"


def _as_pillar(colname, colval, show_type=True):
    coltype = f"<{colval.dtype.name}>"
    display_type = coltype if show_type else ''
    pillar = [colname, display_type] + list(colval.astype(str))
    max_len = max([len(s) for s in pillar])

    justify_right = any([t in coltype for t in ['int', 'float']])

    return [
        s.rjust(max_len) if justify_right else s.ljust(max_len)
        for s in pillar
    ]