#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        import re
        # Replace multiple punctuation marks with a single period
        normalized_value = re.sub(r'[.!?]+', '.', self.value)
        # Split the string by period
        sentences = [s.strip() for s in normalized_value.split('.') if s.strip()]
        return len(sentences)
    pass
