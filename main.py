from attitude import *
from preprocessing import *
from get_from_dataset import *

text = get_sentence_from_dataset("twitterGenerici")

for sentence in text[0::2]:
    attitudeEVA = 0
    attitudeACT = 0
    attitudePOT = 0

    #Elimination of stopwords
    tokens = gavi_tokenize_no_stopwords(sentence)

    print ""
    print tokens

    for t in tokens:
        try:
            #Lexical Analysis of the text
            t = gavi_tokenize_no_puntuaction(t)[0]
        except IndexError:
            pass

        #Stemming of the remaining words with:

        # WordNetLemmatizer
        t = gavi_stemming(t)

        #Lancaster stemming algorithm
        #t = gavi_stemming_lancaster(t)

        #Porter stemming algorithm SBAGLIA LE PAROLE CHE FINISCONO CON Y HAPPY -> HAPPI
        #t = gavi_stemming_porter(t)

        #Stemming of the remaining words with  Lancaster stemming algorithm
        try:
            #Osgood analisys
            attitudeEVA += EVA(t)
            attitudeACT += ACT(t)
            attitudePOT += POT(t)
        except IndexError:
            pass

    print "attitudeEVA:  " + str(attitudeEVA)
    print "attitudeACT:  " + str(attitudeACT)
    print "attitudePOT:  " + str(attitudePOT)

weak = wn.synsets("weak", "a")[0]
print(tree(weak))
word = wn.synsets("weak")[0]
print word.shortest_path_distance(weak)


