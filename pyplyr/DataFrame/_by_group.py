import numpy as np
from collections import OrderedDict
from .._utils import _as_id

def _by_group(self, by, fn):

    mapped_pieces = [fn(data) for data in self._split_by(by)]

    out_colnames = mapped_pieces[0].colnames()

    out = self._new(**{
        col: np.concatenate([df[col] for df in mapped_pieces])
        for col in out_colnames
    })

    return out


def _split_by(self, cols=None):
    cols = cols or []

    if len(cols) == 0:
        return [self]
    
    return [self[split, None] for split in self._make_splits(cols)]
    

def _make_splits(self, cols: list):
    self._check_exists(*cols)

    col_ids = [
        _as_id(colval)
        for colname, colval in self.items()
        if colname in cols
    ]

    group_id = _as_id(np.column_stack(col_ids))
    splits = [group_id == x for x in range(max(group_id) + 1)]

    return splits