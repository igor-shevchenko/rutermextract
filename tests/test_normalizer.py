# coding=utf-8
from __future__ import absolute_import
import unittest
from rutermextract.parser import Parser
from rutermextract.normalizer import Normalizer


class NormalizerTest(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        self.normalizer = Normalizer()

    def normalize(self, words):
        parsed_words = [self.parser(word) for word in words]
        return self.normalizer(parsed_words)

    def test_normalize(self):
        self.assertEqual(self.normalize([u'проверкой']), u'проверка')

    def test_normalize_adjective(self):
        self.assertEqual(self.normalize([u'французских', u'булок']), u'французские булки')

    def test_normalize_genitive_case(self):
        self.assertEqual(self.normalize([u'причину', u'аварии', u'ракеты-носителя']), u'причина аварии ракеты-носителя')

    def test_normalize_neologisms(self):
        self.assertEqual(self.normalize([u'проверка', u'нормалайзера']), u'проверка нормалайзера')
        self.assertEqual(self.normalize([u'нормалайзера']), u'нормалайзер')

    def test_normalize_numbers(self):
        self.assertEqual(self.normalize([u'семь', u'лет']), u'семь лет')
        self.assertEqual(self.normalize([u'семи', u'лет']), u'семь лет')
        self.assertEqual(self.normalize([u'15', u'человек']), u'15 человек')

    def test_latin(self):
        self.assertEqual(self.normalize([u'twitter']), u'twitter')

    def test_unexpected_token_type(self):
        self.assertRaises(Exception, lambda: self.normalize([u'смотреть']))

if __name__ == '__main__':
    unittest.main()
