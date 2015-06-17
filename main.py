from attitude import *
from preprocessing import *
from get_from_dataset import *

from synonym_list import *


text = get_sentence_from_dataset("twitterGenerici")

for sentence in text[0::2]:

    attitude_EVA_ACT_POT = [0, 0, 0]
    attitude_EVA_ACT_POT_temp = [0, 0, 0]

    # print "frase iniziale: " + str(sentence)

    # Converto tutta in lowercase
    sentence = sentence.lower()

    # Elimino la punteggiatura
    try:
        tokens = remove_puntuaction(sentence)
    except IndexError:
        pass

    # Ricreo una stringa invece che una lista di token
    string = ''
    for t in tokens:
        string += str(t)
        string += ' '

    # Elimination of stopwords
    tokens = remove_stopwords(string)

    for t in tokens:

        # Stemming of the remaining words with:

        # WordNetLemmatizer
        # t = gavi_stemming(t)

        # Lancaster stemming algorithm
        # t = gavi_stemming_lancaster(t)

        # Porter stemming algorithm SBAGLIA LE PAROLE CHE FINISCONO CON Y HAPPY -> HAPPI
        # t = gavi_stemming_porter(t)

        # Osgood analisys
        try:
            attitude_EVA_ACT_POT_temp = EVA_ACT_POT(t)

            for i in [0, 1, 2]:
                attitude_EVA_ACT_POT[i] += attitude_EVA_ACT_POT_temp[i]

        except IndexError:
            pass

    print str(sentence) + ' ' + str(attitude_EVA_ACT_POT)