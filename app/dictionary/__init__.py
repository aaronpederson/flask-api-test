from pathlib import Path
from Levenshtein import distance
import re

corpus_path = Path(__file__).parent.parent.parent.joinpath('corpus.txt')
with open(corpus_path, 'r') as corpus:
    data = corpus.read()
    words = list(set(re.split("[\W]+", data)))


def Lookup(word):
    global words
    for w in words:
        if distance(w, word) < 2:
            return w

    return word
