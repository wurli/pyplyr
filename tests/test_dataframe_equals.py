import pyplyr as pyp


def test_dataframe_equals_works():
    
    df1 = pyp.DataFrame(x=['foo', 'bar'], y=[1, 2])
    df2 = pyp.DataFrame(x=['foo', 'bar'], y=[1, 2]) 
    assert pyp.dataframe_equals(df1, df2) == True, "DataFrames with same data are equal"
    
    df2 = pyp.DataFrame(y=[1, 2], x=['foo', 'bar'])
    assert pyp.dataframe_equals(df1, df2) == False, "DataFrames different column orders are not equal"
    
    df2 = pyp.DataFrame(x=['foo', 'bar'])
    assert pyp.dataframe_equals(df1, df2) == False, "DataFrames with different number of columns are not equal"
    
    df2 = pyp.DataFrame(x=['foo', 'bar'], y=[1, 3])
    assert pyp.dataframe_equals(df1, df2) == False, "DataFrames with different data are not equal"
    
    df1 = pyp.DataFrame()
    df2 = pyp.DataFrame()
    assert pyp.dataframe_equals(df1, df2) == True, "Empty DataFrames are equal"
    
    df2 = pyp.DataFrame(x=[])
    assert pyp.dataframe_equals(df1, df2) == False, "Empty DataFrames with different number of columns are not equal"
    
    df1 = pyp.DataFrame(x=[])
    df2 = pyp.DataFrame(x=[])
    assert pyp.dataframe_equals(df1, df2) == True, "Empty DataFrames with same columns are equal"