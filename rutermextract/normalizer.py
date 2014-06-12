# coding=utf-8
class Normalizer(object):
    """
    Нормализация набора токенов в строку в нормальной форме.
    """

    def __call__(self, chunk):
        normalized = []
        for i, token in enumerate(chunk):
            if token.is_adjective() or token.is_participle():
                # Прилагательные и причастия приводятся к именительному падежу.
                normalized.append(token.get_nominal())
            elif token.is_noun():
                # Первое существительное приводится к именительному падежу, а остальные берутся в родительном.
                normalized.append(token.get_nominal())
                normalized.extend(token.get_word() for token in chunk[i+1:])
                break
            elif token.is_number():
                # Число тоже приводится к именительному падежу, а остальное берется как было.
                normalized.append(token.get_nominal())
                normalized.extend(token.get_word() for token in chunk[i+1:])
                break
            elif token.is_latin():
                # Латиница никак не приводится.
                normalized.extend(token.get_word() for token in chunk[i:])
                break
            else:
                raise Exception(u'Unexpected token type: %s' % token)
        return ' '.join(normalized)