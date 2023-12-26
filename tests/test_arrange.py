import pyplyr as pyp
import numpy as np
import numpy.testing as npt

def test_ungrouped_arrange():
    df = pyp.DataFrame(
        x=['foo', 'foo', 'baz', 'baz', 'bar', 'bar'],
        y=[1, 1, 1, 2, 2, 1],
        z=[1, 2, 3, 4, 5, 6]
    ) 

    df1 = df.arrange('x')
    npt.assert_array_equal(df1['x'], np.array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo']), "arrange() should sort by one column")   
    npt.assert_array_equal(df1['y'], np.array([2, 1, 1, 2, 1, 1]), "arrange() should not change other columns")
    
    df2 = df.arrange('x', 'y')
    npt.assert_array_equal(df1['x'], np.array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo']), "arrange() should sort by multiple columns")   
    npt.assert_array_equal(df1['y'], np.array([2, 1, 1, 2, 1, 1]), "arrange() should sort by multiple columns")
    npt.assert_array_equal(df1['z'], np.array([5, 6, 3, 4, 1, 2]), "arrange() should not change other columns")
    
