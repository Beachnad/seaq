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

    def test_to_db(self):
        self.sea_quill.to_db(test_df, 'test')
        df = self.sea_quill.from_db('test')
        self.assertTrue(test_df.equals(df))


