#!/usr/bin/env python3
import io
import sys

class MyString:
    def __init__(self, value=''):
        self.value = value  # This will use the setter method for validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        import re
        normalized_value = re.sub(r'[.!?]+', '.', self.value)
        sentences = [s.strip() for s in normalized_value.split('.') if s.strip()]
        return len(sentences)
    pass