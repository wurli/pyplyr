import numpy as np

def dataframe_equals(x, y):
    x_cols = x.colnames()
    y_cols = y.colnames()
    
    if x_cols != y_cols:
        return False
    
    for col in x_cols:
        if not np.array_equal(x[col], y[col]):
            return False
    
    return True