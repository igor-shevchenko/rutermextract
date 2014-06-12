# coding=utf-8
import re


class Tokenizer(object):
    """
    Токенизация текста на отдельные слова.
    """

    def __call__(self, text):
        tokens = re.split(r'([^\w]*(?:\s|^|$)+[^\w]*)', text, flags=re.UNICODE)
        stripped_tokens = [token.strip() for token in tokens]
        return [token for token in stripped_tokens if token and not token.isspace()]

