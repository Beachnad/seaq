import pandas as pd
from datetime import datetime
from seaq.core import SeaQuill

from unittest import TestCase


test_df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [2.3, 6.1, 3.0],
    'c': ['cats', 'dogs', 'frogs'],
    'd': [datetime(2011, 10, 10), datetime(2011, 10, 10), datetime(2011, 10, 10)],
    'e': ['41', '21', '24']
})


class TestSeaQuill(TestCase):
    sea_quill = SeaQuill(':memory:')

    def test_to_table(self):
        self.sea_quill.to_table(test_df, 'test')
        df = self.sea_quill.from_db('test')
        self.assertTrue(test_df.equals(df))

    def test_metadata(self):
        self.sea_quill.to_table(test_df, 'test')
        metadata = self.sea_quill.read_metadata('test')
        self.assertTrue(metadata.equals(pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'table_name': ['test', 'test', 'test', 'test', 'test'],
            'column_name': ['a', 'b', 'c', 'd', 'e'],
            'original_dtype': ['int64', 'float64', 'object', 'datetime64[ns]', 'object']
        })))


sea_quill = SeaQuill('test.db')
sea_quill.to_table(test_df, 'test')
sea_quill.read_metadata('test')

