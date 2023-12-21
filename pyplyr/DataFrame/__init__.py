from ..DataFrameBase import DataFrameBase


class DataFrame(DataFrameBase):
    def __init__(self, **args):
        super().__init__(**args)

    from .mutate import mutate

    