from nltk.corpus import wordnet as wn
from synonym_list import *

#Il nostro scopo e quello di misurare il significato personale espresso in un testo.
# Per una tale impresa abbia successo,

def disambiguateTerms(terms):
        for t_i in terms:    # t_i is target term
                selSense = None
                selScore = 0.0
                for s_ti in wn.synsets(t_i, wn.NOUN):
                        score_i = 0.0
                        for t_j in terms:    # t_j term in t_i's context window
                                if (t_i==t_j):
                                        continue
                                bestScore = 0.0
                                for s_tj in wn.synsets(t_j, wn.NOUN):
                                        tempScore = s_ti.wup_similarity(s_tj)
                                        if (tempScore>bestScore):
                                                bestScore=tempScore
                                score_i = score_i + bestScore
                        if (score_i>selScore):
                                selScore = score_i
                                selSense = s_ti
                if (selSense is not None):
                        print t_i,": ",selSense,", ",selSense.definition
                        print "Score: ",selScore
                else:
                        print t_i,": --"

def EVA_ACT_POT(word):

    list_position = get_pos_from_base_adj(word)

    for item in list_position:
        if item[0] == 'good':
            distance_from_good = item[1]
        if item[0] == 'bad':
            distance_from_bad = item[1]
        if item[0] == 'active':
            distance_from_active = item[1]
        if item[0] == 'passive':
            distance_from_passive = item[1]
        if item[0] == 'strong':
            distance_from_strong = item[1]
        if item[0] == 'weak':
            distance_from_weak = item[1]

    lista_ret_EVA_ACT_POT = []

    try:
        lista_ret_EVA_ACT_POT.append(EVA(distance_from_bad, distance_from_good))
        lista_ret_EVA_ACT_POT.append(ACT(distance_from_passive, distance_from_active))
        lista_ret_EVA_ACT_POT.append(POT(distance_from_weak, distance_from_strong))

    except UnboundLocalError:
        pass

    return lista_ret_EVA_ACT_POT


def EVA(distance_from_bad, distance_from_good):

    distance_between_good_bad = 4;

    try:
        return (distance_from_bad - distance_from_good)/ \
               float(distance_between_good_bad)

    except TypeError:
        return 0


def ACT(distance_from_passive, distance_from_active):

    distance_between_active_passive = 10;

    try:
        return (distance_from_passive - distance_from_active)/ \
               float(distance_between_active_passive)
    except TypeError:
        return 0


def POT(distance_from_weak, distance_from_strong):

    distance_between_strong_weak = 6;

    try:
        return (distance_from_weak - distance_from_strong)/ \
               float(distance_between_strong_weak)

    except TypeError:
        return 0