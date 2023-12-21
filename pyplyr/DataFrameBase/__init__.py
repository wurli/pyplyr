import numpy as np
    

class DataFrameBase():
    def __init__(self, **args):
        arrays = np.broadcast_arrays(*list(args.values()))
        data = {col: val for col, val in zip(args.keys(), arrays)}
        self.data = data

    from .__repr__ import __repr__
    

    # TODO: implement key: list
    def __setitem__(self, key, value):
        key = self._index_to_col(key)
        self.data[key] = self._as_col(value)


    def __getitem__(self, i):
        if type(i) == list:
            colnames = [self._index_to_col(ii) for ii in i]
            cols = {col: self.data[col] for col in colnames}
            return DataFrameBase(**cols)

        col = self._index_to_col(i)
        return self.data[col].copy()
    

    def _index_to_col(self, i):
        if type(i) == int:
            return list(self.data.keys())[i]
        if type(i) == str:
            return i
        raise KeyError(f"Unsupported index type {type(i)}: check {i}")
    

    def _as_col(self, x):
        _, x = np.broadcast_arrays(self[0], x)
        return x


    def nrow(self):
        return len(self.data)
    

    def ncol(self):
        return len(self.data[self.colnames()[0]])
    

    def colnames(self):
        return list(self.data.keys())