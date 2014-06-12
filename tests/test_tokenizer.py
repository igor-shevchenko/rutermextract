# coding=utf-8
from __future__ import absolute_import
import unittest
from rutermextract.tokenizer import Tokenizer


class TokenizerTest(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_tokenize(self):
        self.assertSequenceEqual(self.tokenizer(u'Раз два три.'),
                                 [u'Раз', u'два', u'три', u'.'])

    def test_tokenize_multiple_sentences(self):
        self.assertSequenceEqual(self.tokenizer(u'Раз два три. Четыре.'),
                                 [u'Раз', u'два', u'три', u'.', u'Четыре', u'.'])

    def test_tokenize_punctuation(self):
        self.assertSequenceEqual(self.tokenizer(u'Раз, два, три.'),
                                 [u'Раз', u',', u'два', u',', u'три', u'.'])

    def test_tokenize_incorrect_punctuation(self):
        self.assertSequenceEqual(self.tokenizer(u'Раз , два , три.'),
                                 [u'Раз', u',', u'два', u',', u'три', u'.'])

    def test_tokenize_dot_in_word(self):
        self.assertSequenceEqual(self.tokenizer(u'Зайди на amazon.com.'),
                                 [u'Зайди', u'на', u'amazon.com', u'.'])

    def test_tokenize_quotes(self):
        self.assertSequenceEqual(self.tokenizer(u'Это "пример" текста.'),
                                 [u'Это', u'"', u'пример', u'"', u'текста', u'.'])
        self.assertSequenceEqual(self.tokenizer(u'"Это пример текста".'),
                                 [u'"', u'Это', u'пример', u'текста', u'".'])

    def test_tokenize_numbers(self):
        self.assertSequenceEqual(self.tokenizer(u'Прошло 20 лет.'),
                                 [u'Прошло', u'20', u'лет', u'.'])
        self.assertSequenceEqual(self.tokenizer(u'Прошло 20.5 лет.'),
                                 [u'Прошло', u'20.5', u'лет', u'.'])
        self.assertSequenceEqual(self.tokenizer(u'Прошло 20,5 лет.'),
                                 [u'Прошло', u'20,5', u'лет', u'.'])

    def test_tokenize_brackets(self):
        self.assertSequenceEqual(self.tokenizer(u'Раз (два) три.'),
                                 [u'Раз', '(', u'два', u')', u'три', u'.'])


if __name__ == '__main__':
    unittest.main()
