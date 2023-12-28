import pyplyr as pyp
import numpy as np
import numpy.testing as npt

# Snapshots using syrupy
# Use pytest --snapshot-update to update snapshots

def test_df_creation():
    df = pyp.DataFrame(
        x=['foo', 'foo', 'bar'],
        y=[11.22, 2.3, 3.4],
        z=[3, 4, 5]
    )
    
    npt.assert_array_equal(df['x'], np.array(['foo', 'foo', 'bar']))
    npt.assert_array_equal(df['y'], np.array([11.22, 2.3, 3.4]))
    npt.assert_array_equal(df['z'], np.array([3, 4, 5]))

def test_df_printing(capsys, snapshot):
    df = pyp.DataFrame(
        x=['foo', 'foo', 'bar'],
        y=[11.22, 2.3, 3.4],
        z=[3, 4, 5]
    ) 
    
    print(df)
    
    captured = capsys.readouterr().out
    assert captured == snapshot
    

def test_empty_df_printing(capsys, snapshot):
    df_nocols = pyp.DataFrame() 
    df_norows = pyp.DataFrame(x=[], y=[])
    
    print(df_nocols)
    print(df_norows)
    
    captured = capsys.readouterr().out
    assert captured == snapshot