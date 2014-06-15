# coding=utf-8
from __future__ import absolute_import
import unittest
from rutermextract.term_extractor import TermExtractor


class TermExtractorTest(unittest.TestCase):
    def setUp(self):
        self.term_extractor = TermExtractor()

    def test_extract_terms(self):
        self.assertItemsEqual(self.term_extractor(u'Налётчика на ювелирный салон в Челябинске осудили на семь лет.',
                                                  strings=True),
                              [u'налётчик', u'ювелирный салон', u'челябинск', u'семь лет'])

    def test_extract_terms_with_custom_weight(self):
        weight = lambda term: len(term.normalized)
        self.assertItemsEqual(self.term_extractor(u'Налётчика на ювелирный салон в Челябинске осудили на восемь лет.',
                                                  weight=weight, strings=True),
                              [u'ювелирный салон', u'восемь лет', u'челябинск',  u'налётчик'])

    def test_extract_terms_with_limit(self):
        weight = lambda term: len(term.normalized)
        self.assertItemsEqual(self.term_extractor(u'Налётчика на ювелирный салон в Челябинске осудили на восемь лет.',
                                                  weight=weight, limit=2, strings=True),
                              [u'ювелирный салон', u'восемь лет'])

    def test_extract_terms_as_terms(self):
        result = self.term_extractor(u'Налётчика на ювелирный салон в Челябинске осудили на семь лет.')
        strings = [term.normalized for term in result]
        self.assertItemsEqual(strings, [u'налётчик', u'ювелирный салон', u'челябинск', u'семь лет'])


if __name__ == '__main__':
    unittest.main()
