from .._utils import _make_col, _to_vector

def summarise(self, **kwargs):
    by = _to_vector(kwargs.pop('_by', None))
    return self.copy()._by_group(by, lambda g: _summarise_group(g, kwargs, by))


def _summarise_group(g, fns, by):
    group_row = [] if len(by) == 0 else [g[[0], _to_vector(by)]]
    summarised = []
    
    for colname, x in fns.items():
        new_col = _make_col(summarised + [g], x)
        
        if len(new_col) != 1:
            raise ValueError("Values must be summarised to a single row")
        
        summarised += [{colname: new_col}]
        
    out_cols = {c: v for df in group_row + summarised for c, v in df.items()}
    
    return g._new(**out_cols)

