# coding=utf-8
from __future__ import absolute_import
import unittest
from rutermextract.term_extractor import TermExtractor


class TermExtractorTest(unittest.TestCase):
    def setUp(self):
        self.term_extractor = TermExtractor()

    def test_extract_terms(self):
        self.assertItemsEqual(self.term_extractor(u'Налётчика на ювелирный салон в Челябинске осудили на семь лет.'),
                              [u'налётчик', u'ювелирный салон', u'челябинск', u'семь лет'])

    def test_extract_terms_with_custom_weight(self):
        weight = lambda pair: len(pair[0])
        self.assertItemsEqual(self.term_extractor(u'Налётчика на ювелирный салон в Челябинске осудили на восемь лет.',
                                                  weight=weight),
                              [u'ювелирный салон', u'восемь лет', u'челябинск',  u'налётчик'])

    def test_extract_terms_with_limit(self):
        weight = lambda pair: len(pair[0])
        self.assertItemsEqual(self.term_extractor(u'Налётчика на ювелирный салон в Челябинске осудили на восемь лет.',
                                                  weight=weight, limit=2),
                              [u'ювелирный салон', u'восемь лет'])


if __name__ == '__main__':
    unittest.main()
