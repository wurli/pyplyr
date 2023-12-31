import numpy as np
from collections import OrderedDict
from .._utils import _as_id, _rm_none, _to_vector

# size == "maintain" => size stays same
# size == "collapse" => groups are collapsed to single row
# size == "any"      => groups may be resized arbitrarily
def _by_group(self, by, fn):
    
    groups, proxy_orderings = self._split_by(by)
    groups = [fn(g) for g in groups]
    
    def new_group_order(ordering, group):
        if group.nrow() == len(ordering):
            return ordering
        return np.broadcast_to(ordering.min(), group.nrow())

    new_orderings = np.argsort(np.concatenate([
        new_group_order(ordering, group)
        for ordering, group in zip(proxy_orderings, groups)
    ]))
    
    out_colnames = groups[0].colnames()

    combined_groups = self._new(**{
        col: np.concatenate([df[col] for df in groups])
        for col in out_colnames
    })
    
    out = combined_groups[new_orderings, None]

    return out


def _split_by(self, by=None):
    by = _rm_none(_to_vector(by))

    if len(by) == 0:
        return [self], [np.array(range(self.nrow()))]
    
    splits = self._make_splits(by)
    row_nums = np.array(range(self.nrow()))
    
    groups = [self[split, None] for split in splits]
    proxy_orderings = [row_nums[split] for split in splits]
    
    return groups, proxy_orderings
    

def _make_splits(self, by: list):
    self._check_exists(*by)

    col_ids = [
        _as_id(colval)
        for colname, colval in self.items()
        if colname in by
    ]

    group_id = _as_id(np.column_stack(col_ids))
    splits = [group_id == x for x in range(max(group_id) + 1)]

    return splits