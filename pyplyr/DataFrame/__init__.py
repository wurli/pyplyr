from ..DataFrameBase import DataFrameBase


class DataFrame(DataFrameBase):
    def __init__(self, **args):
        super().__init__(**args)

    from .mutate import mutate
    
    from ._by_group import _by_group, _make_splits, _split_by


    