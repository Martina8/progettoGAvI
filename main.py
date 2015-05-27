from attitude import *
from preprocessing import *
import nltk

text = "Magic is on the air"

tokens = gavi_tokenize_no_stopwords(text)

print tokens


for t in tokens:
    print t
    t = gavi_stemming(t)
    print EVA(t)
    print ACT(t)
    print POT(t)

