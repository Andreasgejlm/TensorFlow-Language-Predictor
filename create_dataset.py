import os
import numpy as np
import tensorflow as tf
import one_hot_encode_word
import re
import random
import pickle

DATA_FOLDER_DIR = "media/"
LANGUAGES = ["English", "Danish", "German", "French", "Italian", "Spanish"]


def create_data(folder):
    lines = []
    encoder = one_hot_encode_word.OneHotEncode()
    for language in LANGUAGES:
        index_of_language = LANGUAGES.index(language)
        full_path = folder + language + ".txt"
        for line in open(full_path, 'rb'):
            line = line.decode('unicode_escape')
            line = re.sub(r'\s+|\.|\/', '', line)
            if len(line) <= 10:
                line = line.lower()
                line_one_hot = encoder.encode(line)
                lines.append([line_one_hot, index_of_language])
    random.shuffle(lines)
    words = []
    labels = []
    for word, label in lines:
        words.append(word)
        labels.append(label)
    words = np.array(words)
    labels = np.array(labels)
    return words, labels


X, y = create_data(DATA_FOLDER_DIR)

pickle_out = open('X.pickle', "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open('y.pickle', "wb")
pickle.dump(y, pickle_out)
pickle_out.close()
