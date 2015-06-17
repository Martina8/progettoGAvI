import nltk
from nltk.stem.wordnet import WordNetLemmatizer as wnl
from nltk.corpus import wordnet_ic # per la def similarity
from nltk.corpus import wordnet as wn
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import	stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer


nltk.stem.porter


def remove_puntuaction(text):
    tokenizer = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
    text = tokenizer.tokenize(text)
    # print 'testo senza punteggiatura' + str(text)
    return text


def remove_stopwords(text):
    tokens = nltk.word_tokenize(text)
    words = []
    wnl = nltk.WordNetLemmatizer()
    for t in tokens:
        if not t in stopwords.words('english'):
            words.append(wnl.lemmatize(t))
    return words


#Porta le parole alla loro forma base. Es: cars -> car
def nltk_stemming(word):
    lmtzr = wnl()
    return lmtzr.lemmatize(word)

#Stamming Lancaster stemming algorithm
def gavi_stemming_lancaster(word):
    st = LancasterStemmer()
    return st.stem(word)

#Stamming Porter stemming algorithm
def gavi_stemming_porter(word):
    sp = PorterStemmer()
    return sp.stem(word)

def gavi_morphy(word):
    return wn.morphy(word)

