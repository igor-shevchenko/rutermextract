# coding=utf-8
class Extractor(object):
    """
    Извлечение из текста ключевых слов (в виде списка токенов) в соответствии с поданной IOB-последовательностью.

    Если аргумент nested установлен в True, то извлекаются еще и вложенные тёрмы.
    Например, вместе с "функциональный язык программирования" извлекаются "язык программирования" и "программирование".
    """
    def __call__(self, tokens, iob_sequence, nested=False):
        # Список блоков, представленых в виде списка токенов.
        # Если nested равен False, то в списке всегда один блок.
        chunks = []

        for token, label in zip(tokens, iob_sequence):
            if len(chunks) and label in ['O', 'B']:
                for chunk in chunks:
                    yield chunk
                chunks = []

            if label == 'I':
                for chunk in chunks:
                    chunk.append(token)

            if label == 'B' or nested and label == 'I':
                chunks.append([token])

        if len(chunks):
            for chunk in chunks:
                yield chunk