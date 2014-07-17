from __future__ import absolute_import
import unittest
from rutermextract.extractor import Extractor


class ExtractorTest(unittest.TestCase):
    def setUp(self):
        self.extractor = Extractor()

    def test_extract(self):
        self.assertListEqual(list(self.extractor([1, 2, 3, 4, 5, 6, 7], 'BIIOBBO')), [[1, 2, 3], [5], [6]])

    def test_extract_final_chunk(self):
        self.assertListEqual(list(self.extractor([1, 2, 3, 4, 5, 6, 7], 'BIIOBBI')), [[1, 2, 3], [5], [6, 7]])

    def test_extract_nested(self):
        self.assertListEqual(list(self.extractor([1, 2, 3, 4, 5, 6, 7], 'BIIOBBO', nested=True)),
                             [[1, 2, 3], [2, 3], [3], [5], [6]])

    def test_extract_final_chunk_nested(self):
        self.assertListEqual(list(self.extractor([1, 2, 3, 4, 5, 6, 7], 'BIIOBBI', nested=True)),
                             [[1, 2, 3], [2, 3], [3], [5], [6, 7], [7]])



if __name__ == '__main__':
    unittest.main()
