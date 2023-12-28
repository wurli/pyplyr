import numpy as np
from collections import OrderedDict
from ..DataFrameCols import DataFrameCols

def __getitem__(self, pos):
    if not isinstance(pos, tuple):
        pos = (None, pos)

    i, j = pos

    # Handle cases where j contains numbers
    j = self.as_colname(j)

    out = self.copy()._subset_rows(i)[j]

    if isinstance(out, DataFrameCols):
        scalar_cols = not all([isinstance(col, np.ndarray) for col in out.values()])
        if scalar_cols:
            return out
        else:
            return self._new(**out)
        
    return out


def _subset_rows(self, i):
    if i is None:
        return DataFrameCols(**self)
    
    if isinstance(i, list) or isinstance(i, np.ndarray):
        i = [ii for ii in i if ii is not None]
     
    return DataFrameCols(**{col: self[col][i] for col in self.colnames()})

