# coding=utf-8
from collections import Counter
from .tokenizer import Tokenizer
from .parser import Parser
from .labeler import IOBLabeler
from .extractor import Extractor
from .normalizer import Normalizer
from .ranker import Ranker


class TermExtractor(object):
    """
    Извлечение ключевых слов из текста.
    """

    def __init__(self, tokenizer=None, parser=None, labeler=None, extractor=None, normalizer=None, ranker=None):
        self.tokenizer = tokenizer or Tokenizer()
        self.parser = parser or Parser()
        self.labeler = labeler or IOBLabeler()
        self.extractor = extractor or Extractor()
        self.normalizer = normalizer or Normalizer()
        self.ranker = ranker or Ranker()

    def __call__(self, text, limit=None, weight=None):
        tokens = self.tokenizer(text)
        parsed_tokens = map(self.parser, tokens)
        iob_sequence = self.labeler(parsed_tokens)
        chunks = self.extractor(parsed_tokens, iob_sequence)
        normalized_chunks = map(self.normalizer, chunks)
        counted_chunks = Counter(normalized_chunks)
        sorted_chunks = self.ranker(counted_chunks, weight=weight)
        return sorted_chunks[:limit]