from attitude import *
from preprocessing import *
from get_from_dataset import *

text = get_sentence_from_dataset("twitterGenerici")

tokens = gavi_tokenize_no_stopwords(text[0])

print tokens

for t in tokens:
    print t
    t = gavi_stemming(t)
    print EVA(t)
    print ACT(t)
