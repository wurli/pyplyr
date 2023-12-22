import numpy as np
from ..DataFrameCols import DataFrameCols

class DataFrameBase(DataFrameCols):
    def __init__(self, **kwargs):
        arrays = np.broadcast_arrays(*list(kwargs.values()))
        self = super().__init__(**{
            key: arr for key, arr in zip(kwargs.keys(), arrays)
        })
    
    from .__repr__    import __repr__
    from .__getitem__ import __getitem__, _subset_rows


    # TODO: implement key: list
    def __setitem__(self, key, value):
        key = self.as_colname(key)
        old_cols = self.colnames()
        col_is_new = key not in old_cols
        DataFrameCols.__setitem__(self, key, self._make_col(value))

        if col_is_new:
            self = self.reorder(key, after=-1)
        else:
            self = self.reorder(old_cols)
    

    def _check_exists(self, *args):
        non_existant = set(args) - set(self.colnames())
        if len(non_existant) > 0:
            non_existant = ", ".join(non_existant)
            raise KeyError(f"Non-existant column(s): check {non_existant}")
    

    def _make_col(self, x):
        _, x = np.broadcast_arrays(self[0], x)
        return x


    def nrow(self):
        return len(self[0])

    
