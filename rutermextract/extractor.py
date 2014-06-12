# coding=utf-8
class Extractor(object):
    """
    Извлечение из текста ключевых слов (в виде списка токенов) в соответствии с поданной IOB-последовательностью.
    """
    def __call__(self, tokens, iob_sequence):
        chunk = []
        for token, label in zip(tokens, iob_sequence):
            if len(chunk) and label in ['O', 'B']:
                yield chunk
                chunk = []
            if label in ['I', 'B']:
                chunk.append(token)
        if len(chunk):
            yield chunk