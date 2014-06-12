# coding=utf-8
from __future__ import absolute_import
import unittest
from rutermextract.parser import Parser
from rutermextract.labeler import IOBLabeler


class LabelerTest(unittest.TestCase):
    def setUp(self):
        self.labeler = IOBLabeler()
        self.parser = Parser()

    def label(self, words):
        parsed_words = map(self.parser, words)
        return ''.join(self.labeler(parsed_words))

    def test_label(self):
        self.assertEqual(self.label([u'Съешь', u'еще', u'этих', u'мягких', u'французских', u'булок', u'да', u'выпей',
                                     u'же', u'чаю', u'.']), 'OOOBIIOOOBO')

    def test_label_genitive_case(self):
        self.assertEqual(self.label([u'Роскосмос', u'назвал', u'причину', u'аварии', u'ракеты-носителя', u'.']),
                         'BOBIIO')

    def test_label_dative_case(self):
        self.assertEqual(self.label([u'Человек', u'собаке', u'друг', u',', u'это', u'знают', u'все', u'вокруг', u'.']),
                         'BBBOOOOOO')

    def test_label_number(self):
        self.assertEqual(self.label([u'Налётчика', u'на', u'ювелирный', u'салон', u'в', u'Челябинске', u'осудили',
                                     u'на', u'семь', u'лет', u'.']), 'BOBIOBOOBIO')
        self.assertEqual(self.label([u'Житель', u'Челябинска', u'получил', u'условный', u'срок', u'за', u'хищение',
                                     u'38', u'тонн', u'ферросплавов', u'.']), 'BIOBIOBBIIO')

    def test_label_latin(self):
        self.assertEqual(self.label([u'Библиотека', u'rutermextract', u'для', u'извлечения', u'ключевых', u'слов', u'.']),
                         'BIOBBIO')

    def test_label_isolated_adjective(self):
        self.assertEqual(self.label([u'Ничего', u'хорошего', u'в', u'этом', u'нет', u'.']),
                         'OOOOOO')


if __name__ == '__main__':
    unittest.main()
