from __future__ import absolute_import
import unittest
from rutermextract.extractor import Extractor


class ExtractorTest(unittest.TestCase):
    def setUp(self):
        self.extractor = Extractor()

    def test_extract(self):
        self.assertListEqual(list(self.extractor([1, 2, 3, 4, 5, 6], 'BIOBBO')), [[1, 2], [4], [5]])

    def test_extract_final_chunk(self):
        self.assertListEqual(list(self.extractor([1, 2, 3, 4, 5, 6], 'BIOBBI')), [[1, 2], [4], [5, 6]])


if __name__ == '__main__':
    unittest.main()
