# coding=utf-8
class Ranker(object):
    """
    Сортировка ключевых слов. Можно указать свою функцию для вычисления веса ключевого слова.
    """

    def __call__(self, counter, weight=None):
        if weight is None:
            # По умолчанию ключевые слова упорядочиваются по количеству употреблений.
            weight = lambda word_count_pair: (word_count_pair[1], word_count_pair[0])
        sorted_items = sorted(counter.iteritems(), key=weight, reverse=True)
        return [item[0] for item in sorted_items]