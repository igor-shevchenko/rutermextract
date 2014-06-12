# coding=utf-8
from enum import Enum


class LabelerStates(Enum):
    """
    Возможные состояния лейблера:
    search - поиск ключевого слова,
    adj - встретилось одно или несколько прилагательных (а также числительных или причастий),
    noun - встретилось одно или несколько существительных.
    """

    search, adj, noun = range(3)


class IOBLabeler(object):
    """
    Получение IOB-последовательности, соответствующей ключевым словам в тексте.
    IOB-последовательость содержит метку для каждого токена текста.
    "B" - токен является началом ключевого слова,
    "I" - токен находится внутри ключевого слова,
    "O" - токен находится вне ключевого слова.
    Ключевые слова имеют примерно такой вид: <adj>* <noun>+
    """

    def __call__(self, words):
        state = LabelerStates.search

        # Встретив прилагательное, нельзя сразу сказать, относится ли оно к ключевому слову.
        # Поэтому будем хранить количество встреченных прилагательных
        number_of_adj = 0

        for word in words:
            if not word:
                # Если не удалось отпарсить, то сбрасываем.
                while number_of_adj:
                    yield 'O'
                    number_of_adj -= 1
                yield 'O'
                state = LabelerStates.search
            elif word.is_number() or word.is_adjective() or word.is_participle():
                # Встретилось что-то, что может идти перед существительными: число, прилагательное, причастие.
                state = LabelerStates.adj
                number_of_adj += 1
            elif word.is_latin():
                # Латинское слово в тексте - наверняка название чего-то, считаем его существительным в любом падеже.
                if state == LabelerStates.search:
                    yield 'B'
                elif state == LabelerStates.adj:
                    yield 'B'
                    while number_of_adj:
                        yield 'I'
                        number_of_adj -= 1
                else:
                    yield 'I'
                state = LabelerStates.noun
            elif word.is_noun() and state != LabelerStates.noun:
                # Встретилось существительное (после прилагательного или само по себе).
                if state == LabelerStates.search:
                    yield 'B'
                else:
                    yield 'B'
                    while number_of_adj:
                        yield 'I'
                        number_of_adj -= 1
                state = LabelerStates.noun
            elif word.is_noun() and word.is_genitive():
                # Существительное в родительном падеже после другого существительного. Например, "министерство обороны".
                yield 'I'
                state = LabelerStates.noun  # останемся в состоянии NOUN для длинных цепочек существительных
            elif word.is_noun():
                # Существительное не в родительном падеже после другого существительного.
                # Например, "человек собаке друг". Начнем отсюда новое ключевое слово.
                yield 'B'
                state = LabelerStates.noun
            else:
                # Другие части речи (предлоги, глаголы). Перейдем в состояние поиска.
                while number_of_adj:
                    yield 'O'
                    number_of_adj -= 1
                yield 'O'
                state = LabelerStates.search