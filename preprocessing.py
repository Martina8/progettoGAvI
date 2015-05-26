import nltk
from nltk.stem.wordnet import WordNetLemmatizer as wnl
from nltk.corpus import wordnet_ic # per la def similarity
from nltk.corpus import wordnet as wn


def gavi_tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens

def gavi_tokenize_with_morphy(text):
    tokens = nltk.word_tokenize(text)
    return nltk.pos_tag(tokens)

def gavi_tokenize_no_stopwords(text):
    tokens = nltk.word_tokenize(text)
    words = []
    from nltk.corpus import	stopwords
    wnl = nltk.WordNetLemmatizer()
    for t in tokens:
            if not t in stopwords.words('english'):
                    words.append(wnl.lemmatize(t))
    return words

def gavi_synset(word):
    return wn.synset(word)

#Ritorna un punteggio che denota quanto due parole siano simili, in base alla profondita dei due sensi nella
#tassonomia e sulla loro Least Common Subsumer.
def gavi_similarity_wup(w1, w2):
    return w1.wup_similarity(w2)

def gavi_similarity(w1, w2):
    brown_ic = wordnet_ic.ic('ic-brown.dat')
    return w1.res_similarity(w2,brown_ic)

#Porta le parole alla loro forma base. Es: cars -> car
def gavi_stemming(word):
    lmtzr = wnl()
    return lmtzr.lemmatize(word)

def gavi_morphy(word):
    return wn.morphy(word)

