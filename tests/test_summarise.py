import pyplyr as pyp
import numpy as np
import numpy.testing as npt

def test_summarise_works():
    df = pyp.DataFrame(
        x=['foo', 'foo', 'bar', 'foo'], 
        y=[11.22, 2.3, 3.4, 100], 
        z=[1, 1, 2, 3]
    )

    df.summarise(a=lambda y: y.sum())

