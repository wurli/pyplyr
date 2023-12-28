from .._utils import _reorder
import copy    
import numpy as np

class DataFrameCols(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def __getitem__(self, pos):
        if pos is None:
            return self

        pos = self.as_colname(pos)
        
        if isinstance(pos, list) or isinstance(pos, np.ndarray):
            return DataFrameCols(**{p: self[p] for p in pos if pos})
        
        return super().__getitem__(pos)


    def reorder(self, cols, after = None):

        # TODO: check all keys exist
        # TODO: check after is scalar
        after = self.as_colnum(after)

        new_cols = _reorder(self.colnames(), cols, after)

        return self._new(**{col: self[col] for col in new_cols})


    def colnames(self):
        return list(self.keys())
    
    
    def ncol(self):
        return len(self.colnames())
    

    def as_colname(self, i):
        if i is None or isinstance(i, str):
            return i
        if isinstance(i, int):
            return self.colnames()[i]
        if isinstance(i, list) or isinstance(i, np.ndarray):
            i = [ii for ii in i if ii is not None]
            return [self.as_colname(ii) for ii in i]
        raise KeyError(f"Cannot get index of type {type(i)}")
    

    def as_colnum(self, i):
        if i is None or isinstance(i, int):
            return i
        if isinstance(i, str):
            return self.colnames().index(i)
        if isinstance(i, list):
            return [self.as_colname(ii) for ii in i]
        raise KeyError(f"Cannot get get index of type {type(i)}")
    
    
    def copy(self):
        return self.__class__(**copy.copy(dict(self)))
    
        
    def _new(self, **kwargs):
        return self.__class__(**kwargs)