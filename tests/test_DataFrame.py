import pyplyr as pyp
import numpy as np
import numpy.testing as npt

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
    snapshot.snapshot_dir = 'tests/snapshots'
    
    df = pyp.DataFrame(
        x=['foo', 'foo', 'bar'],
        y=[11.22, 2.3, 3.4],
        z=[3, 4, 5]
    ) 
    
    print(df)
    
    captured = capsys.readouterr()
    snapshot.assert_match(captured.out, 'test_df_printing.txt')