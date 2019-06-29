import numpy as np
class OneHotEncode:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyzáàã-'æøåâéëîèêûçïôñüùöäßòìúíó"
        self.char_to_int = dict((c, i) for i, c in enumerate(self.alphabet))

    def encode(self, word):
        integer_encoded = [self.char_to_int[char] for char in word]
        one_hot_encoded = list()
        for value in integer_encoded:
            letter = [0 for _ in range(len(self.alphabet))]
            letter[value] = 1
            one_hot_encoded.append(letter)
        missing_letters = 10 - len(one_hot_encoded)
        for n in range(missing_letters):
            one_hot_encoded.append(self.create_zeros())
        return one_hot_encoded

    def create_zeros(self):
        zeros = []
        for i in range(len(self.alphabet)):
            zeros.append(0)
        return zeros