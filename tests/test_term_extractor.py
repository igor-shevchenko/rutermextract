# coding=utf-8
from __future__ import absolute_import
import unittest
from rutermextract.term_extractor import TermExtractor


class TermExtractorTest(unittest.TestCase):
    def setUp(self):
        self.term_extractor = TermExtractor()

    def assertTermsEqual(self, first, second):
        # Во втором и третьем питонах методы для проверки последовательностей без учета порядка называются по-разному.
        import sys
        if sys.version_info >= (3, 0):
            self.assertCountEqual(first, second)
        else:
            self.assertItemsEqual(first, second)

    def test_extract_terms(self):
        self.assertTermsEqual(self.term_extractor(u'Налётчика на ювелирный салон в Челябинске осудили на семь лет.',
                                                  strings=True),
                              [u'налётчик', u'ювелирный салон', u'челябинск', u'семь лет'])

    def test_extract_terms_with_custom_weight(self):
        weight = lambda term: len(term.normalized)
        self.assertListEqual(self.term_extractor(u'Налётчика на ювелирный салон в Челябинске осудили на восемь лет.',
                                                 weight=weight, strings=True),
                             [u'ювелирный салон', u'восемь лет', u'челябинск',  u'налётчик'])

    def test_extract_terms_with_limit(self):
        weight = lambda term: len(term.normalized)
        self.assertListEqual(self.term_extractor(u'Налётчика на ювелирный салон в Челябинске осудили на восемь лет.',
                                                 weight=weight, limit=2, strings=True),
                             [u'ювелирный салон', u'восемь лет'])

    def test_extract_terms_as_terms(self):
        result = self.term_extractor(u'Налётчика на ювелирный салон в Челябинске осудили на семь лет.')
        strings = [term.normalized for term in result]
        self.assertTermsEqual(strings, [u'налётчик', u'ювелирный салон', u'челябинск', u'семь лет'])

    def test_extract_without_duplicates(self):
        self.assertListEqual(self.term_extractor(u'Проверка, проверка.', strings=True), [u'проверка'])

    def test_extract_terms_with_nested(self):
        self.assertTermsEqual(self.term_extractor(u'Налётчика на ювелирный салон в Челябинске осудили на семь лет.',
                                                  strings=True, nested=True),
                              [u'налётчик', u'ювелирный салон', u'салон', u'челябинск', u'семь лет', u'года'])


if __name__ == '__main__':
    unittest.main()
