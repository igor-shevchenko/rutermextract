# coding=utf-8
import pymorphy2


class ParsedWord(object):
    """
    Обёртка над результатом разбора pymorphy2.
    """

    def __init__(self, parsed):
        # Используется самый вероятный вариант разбора.
        self.parsed = parsed[0]

    def pos_is(self, pos):
        return self.parsed.tag.POS == pos

    def case_is(self, case):
        return self.parsed.tag.case == case

    def has_grammeme(self, grammeme):
        return grammeme in self.parsed.tag.grammemes

    def is_noun(self):
        return self.pos_is('NOUN')

    def is_adjective(self):
        return (self.pos_is('ADJF') and
                not self.has_grammeme('Anph'))  # ADJF может быть и местоимением ('этот', 'такой'), что нам не подходит.

    def is_participle(self):
        return self.pos_is('PRTF')

    def is_number(self):
        return self.pos_is('NUMR') or self.has_grammeme('NUMB')

    def is_latin(self):
        return self.has_grammeme('LATN')

    def is_genitive(self):
        return self.case_is('gent')

    def get_nominal(self, dependable_noun=None):
        gr = {'nomn'}
        # если есть существительное, то у зависимого от него прилагательного или причастия 
        # пробуем сопоставить род и число
        # увы, нужно проверять на наличие значений в тэгах OpenCorpora,
        # т.к. не у всех слов они полностью заполнены, и pymorphy падает
        if dependable_noun and dependable_noun.parsed.tag.gender:
            gr.add(dependable_noun.parsed.tag.gender)
        if dependable_noun and dependable_noun.parsed.tag.number:
            gr.add(dependable_noun.parsed.tag.number)
        inflected = self.parsed.inflect(gr)
        if not inflected and dependable_noun:
            gr.remove(dependable_noun.parsed.tag.gender)
            inflected = self.parsed.inflect(gr)
        if inflected:
            return inflected.word
        # Слово не удаётся просклонять (например, это число)
        return self.parsed.word

    def get_word(self):
        return self.parsed.word

    def __unicode__(self):
        return self.parsed.word

    def __str__(self):
        return self.parsed.word


class Parser(object):
    """
    Морфологический парсер (обёртка над pymorphy2).
    """

    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()

    def __call__(self, word):
        parsed_word = self.morph.parse(word)
        if parsed_word:
            return ParsedWord(parsed_word)
        return None
