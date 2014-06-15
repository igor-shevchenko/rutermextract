# coding=utf-8
class Ranker(object):
    """
    Сортировка ключевых слов. Можно указать свою функцию для вычисления веса ключевого слова.
    """

    def __call__(self, terms, weight=None):
        if weight is None:
            # По умолчанию ключевые слова упорядочиваются по количеству употреблений, затем - по количеству слов.
            weight = lambda term: (term.count, term.word_count, term.normalized)
        return sorted(terms, key=weight, reverse=True)