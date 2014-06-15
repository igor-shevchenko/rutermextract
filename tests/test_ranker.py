from __future__ import absolute_import
import unittest
from rutermextract.ranker import Ranker
from rutermextract.term_extractor import Term


class RankerTest(unittest.TestCase):
    def setUp(self):
        self.ranker = Ranker()

    def test_rank(self):
        terms = [Term(['1'], '1', 1), Term(['2', '2'], '2', 2), Term(['3', '3', '3'], '3', 3)]
        self.assertListEqual(list(self.ranker(terms)), [terms[2], terms[1], terms[0]])

    def test_rank_with_weight(self):
        terms = [Term(['1'], '1', 1), Term(['2', '2'], '2', 2), Term(['3', '3', '3'], '3', 3)]
        idf = {'1': 1, '2': 0.3, '3': 0.25}
        weight = lambda term: idf.get(term.normalized, 1.0) * term.count
        self.assertListEqual(list(self.ranker(terms, weight=weight)), [terms[0], terms[2], terms[1]])


if __name__ == '__main__':
    unittest.main()
