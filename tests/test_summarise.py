import pytest
import pyplyr as pyp
import numpy as np
import numpy.testing as npt

def test_ungrouped_summarise_works():
    df = pyp.DataFrame(
        x=['foo', 'foo', 'bar', 'foo'], 
        y=[4, 5, 6, 7], 
        z=[1, 2, 3, 4]
    )
    
    df2 = df.summarise(a=lambda y: y.sum())
    assert df2.colnames() == ['a'], "summarise() should return a single-column DataFrame"
    assert df2[0, 'a'] == 22,       "summarise() should sum values correctly"
    
    df2 = df.summarise(a=1, b=lambda a: a + 1)
    assert df2.colnames() == ['a', 'b'], "summarise() should return cols in correct order"
    assert df2[0, 'b'] == 2,             "summarise() should make calculated cols available in subsequent calculations"
    
    df2 = df.summarise(y=1, z = lambda z, y: y + z.sum())
    assert df2.colnames() == ['y', 'z'], "summarise() should return cols in correct order"
    assert df2[0, 'y'] == 1,             "summarise() should produce correct values"
    assert df2[0, 'z'] == 11,            "summarise() should produce correct values"
    
    with pytest.raises(ValueError) as e:
        df.summarise(x=lambda x: x)
    assert "Values must be summarised to a single row" in str(e.value), "summarise() should throw error when fn returns multiple rows"
    

def test_grouped_summarise_works():
    df = pyp.DataFrame(
        x=['foo', 'foo', 'bar', 'foo'], 
        y=[4, 5, 6, 7], 
        z=[1, 1, 3, 4]
    ) 
    
    df2 = df.summarise(y=lambda y: y.sum(), _by='x')
    assert df2.colnames() == ['x', 'y'],                        "summarise() should return a two-column DataFrame"
    npt.assert_array_equal(df2['x'], np.array(['foo', 'bar'])), "summarise() should group correctly"
    npt.assert_array_equal(df2['y'], np.array([16, 6])),        "summarise() should summarise correctly"
    
    df2 = df.summarise(y=lambda y: y.sum(), _by=['x', 'z'])
    assert df2.colnames() == ['x', 'z', 'y'],                          "summarise() should return a three-column DataFrame"
    npt.assert_array_equal(df2['x'], np.array(['foo', 'bar', 'foo'])), "summarise() should order groups correctly"
    npt.assert_array_equal(df2['z'], np.array([1, 3, 4])),             "summarise() should order groups correctly"
    npt.assert_array_equal(df2['y'], np.array([9, 6, 7])),             "summarise() should summarise correctly"
