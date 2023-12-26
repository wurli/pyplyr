import pyplyr as pyp
import numpy.testing as npt
import numpy as np

def test_ungroup_mutate_works():
    df = pyp.DataFrame(
        x=['foo', 'foo', 'bar'],
        y=[11.22, 2.3, 3.4],
        z=[3, 4, 5]
    )
    
    df1 = df.mutate(a = 1)
    npt.assert_array_equal(df1['a'], np.array([1, 1, 1]),             "mutate() should work with a scalar")
    npt.assert_array_equal(df1['x'], np.array(['foo', 'foo', 'bar']), "mutate() should not change other columns")
    
    df2 = df.mutate(a = [1, 2, 3])
    npt.assert_equal(df2['a'], np.array([1, 2, 3]),             "mutate() should work with a list")
    npt.assert_equal(df2['x'], np.array(['foo', 'foo', 'bar']), "mutate() should not change other columns")
    
    df3 = df.mutate(a=lambda y: y + 1)
    npt.assert_array_equal(df3['a'], np.array([12.22, 3.3, 4.4]),     "mutate() should work with a function")
    npt.assert_array_equal(df3['x'], np.array(['foo', 'foo', 'bar']), "mutate() should not change other columns")
    
    df4 = df.mutate(a=lambda y, z: y + z)
    npt.assert_array_equal(df4['a'], np.array([14.22, 6.3, 8.4]),     "mutate() should work with a multi-argument function")
    npt.assert_array_equal(df4['x'], np.array(['foo', 'foo', 'bar']), "mutate should not change other columns")
    
    df5 = df.mutate(y=1)
    npt.assert_array_equal(df5['y'], np.array([1, 1, 1]), "mutate() should allow replacements")
    assert df5.colnames() == ['x', 'y', 'z'], "mutate() should not change column order"


def test_grouped_mutate_works():
    df = pyp.DataFrame(
        x=['foo', 'foo', 'bar'],
        y=[11.22, 2.3, 3.4],
        z=[3, 4, 5]
    ) 
    
    df1 = df.mutate(a=lambda y: y.max(), _by='x')
    npt.assert_array_equal(df1['a'], np.array([11.22, 11.22, 3.4]), "Grouped mutate should work with a function")
    npt.assert_array_equal(df1['x'], np.array(['foo', 'foo', 'bar']), "Grouped mutate should not change other columns") 
    