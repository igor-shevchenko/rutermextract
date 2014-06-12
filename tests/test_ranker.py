from __future__ import absolute_import
import unittest
from rutermextract.ranker import Ranker


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ranker = Ranker()

    def test_rank(self):
        counter = {1: 1, 2: 2, 3: 3}
        self.assertListEqual(list(self.ranker(counter)), [3, 2, 1])

    def test_rank_with_weight(self):
        counter = {1: 1, 2: 2, 3: 3}
        idf = {1: 1, 2: 0.3, 3: 0.25}
        weight = lambda word_count_pair: idf.get(word_count_pair[0], 1.0) * word_count_pair[1]
        self.assertListEqual(list(self.ranker(counter, weight=weight)), [1, 3, 2])


if __name__ == '__main__':
    unittest.main()
