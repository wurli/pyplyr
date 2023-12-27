"""
Within this set of tests, 'extracting' refers to pulling out the contents of
an indifidual column or row, while 'subsetting' refers to simply cutting 
down a DataFrame to produce another DataFrame with possibly less data.
"""

import pyplyr as pyp
from pyplyr import dataframe_equals as eq
import numpy as np
import numpy.testing as npt


def test_extracting_cols_works():
    df = pyp.DataFrame(x=['foo', 'bar'], yy=[1, 2])
    
    npt.assert_array_equal(df['x'], np.array(['foo', 'bar']), "Extracting works with column names")
    npt.assert_array_equal(df['yy'], np.array([1, 2]),        "Extracting works with column names")
    
    npt.assert_array_equal(df[0], np.array(['foo', 'bar']),   "Extracting works with indices")
    npt.assert_array_equal(df[1], np.array([1, 2]),           "Extracting works with indices")
    
    assert eq(df[None], df), "Extracting with None returns original DataFrame"


def test_subsetting_cols_works():
    df1 = pyp.DataFrame(x=['foo', 'bar'], yy=[1, 2])
    
    assert eq(df1[['x', 'yy']], df1), "Subsetting with multiple columns works"
    assert eq(df1[[0, 1]], df1),      "Subsetting with multiple columns works"
    
    df2 = pyp.DataFrame(yy=[1, 2], x=['foo', 'bar'])
    assert eq(df1[['yy', 'x']], df2), "Subsetting with multiple columns produces correct order"
    assert eq(df1[[1, 0]], df2),      "Subsetting with multiple columns produces correct order"
    
    df2 = pyp.DataFrame(x=['foo', 'bar'])
    assert eq(df1[['x']], df2), "Subsetting a single column works"
    assert eq(df1[[0]],   df2), "Subsetting a single column works"
    
    assert eq(df1[[]], pyp.DataFrame()),           "Subsetting with an empty list gives an empty dataframe"
    assert eq(df1[[None]], pyp.DataFrame()),       "Subsetting with [None] gives an empty dataframe"
    assert eq(df1[[None, None]], pyp.DataFrame()), "Subsetting with mutliple Nones gives an empty dataframe"
    

def test_extracting_rows_works():
    df = pyp.DataFrame(x=['foo', 'bar'], yy=[1, 2])
    
    assert df[0, None] == dict(x='foo', yy=1), "Extracting works with indices"
    assert df[1, None] == dict(x='bar', yy=2), "Extracting works with indices"
    
    assert eq(df[None, None], df),             "Extracting with None returns original DataFrame"


def test_subsetting_rows_works():
    df1 = pyp.DataFrame(x=['foo', 'bar'], yy=[1, 2])
    
    df2 = pyp.DataFrame(x=['foo'], yy=[1])
    assert eq(df1[[0], None], df2), "Subsetting a single row works"
    
    df2 = pyp.DataFrame(x=['bar'], yy=[2])
    assert eq(df1[[1], None], df2), "Subsetting a single row works"
    
    assert eq(df1[[0, 1], None], df1), "Subsetting multiple rows works"
    
    df2 = pyp.DataFrame(x=['bar', 'foo'], yy=[2, 1])
    assert eq(df1[[1, 0], None], df2), "Subsetting rows preserves order"
    
    df2 = pyp.DataFrame(x=np.array(['foo'])[[]], yy=np.array([1])[[]])
    assert eq(df1[[], None], df2),           "Subsetting with an empty list gives an empty dataframe"
    assert eq(df1[[None], None], df2),       "Subsetting with [None] gives an empty dataframe"
    assert eq(df1[[None, None], None], df2), "Subsetting with multiple Nones gives an empty dataframe"


