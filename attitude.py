from nltk.corpus import wordnet as wn

#Il nostro scopo e quello di misurare il significato personale espresso in un testo. Per una tale impresa abbia successo,

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

def EVA(word):
    good = wn.synsets("good")[0]
    bad  = wn.synsets("bad")[0]
    word = wn.synsets(word)[0]

    print ""
    print "(" + str(word.shortest_path_distance(bad)) + " - " + str(word.shortest_path_distance(good)) + ")/" + \
          str(good.shortest_path_distance(bad))

    return (word.shortest_path_distance(bad) - word.shortest_path_distance(good))/ float(good.shortest_path_distance(bad))

def ACT(word):
    active = wn.synsets("active")[0]
    passive  = wn.synsets("passive")[0]
    word = wn.synsets(word)[0]

    print ""
    print "(" + str(word.shortest_path_distance(passive)) + " - " + str(word.shortest_path_distance(active)) \
          + ")/" + str(active.shortest_path_distance(passive)) + " = "
    return (word.shortest_path_distance(passive) - word.shortest_path_distance(active))/ float(active.shortest_path_distance(passive))

def POT(word):
    strong = wn.synsets("strong")[0]
    weak  = wn.synsets("weak")[0]
    word = wn.synsets(word)[0]

    print ""
    print "(" + str(word.shortest_path_distance(weak)) + " - " + str(word.shortest_path_distance(strong)) \
          + ")/" + str(strong.shortest_path_distance(weak)) + " = "
    return (word.shortest_path_distance(weak) - word.shortest_path_distance(strong))/ float(strong.shortest_path_distance(weak))

def common(w1, w2):
    print ""
    print "Common_lemmas tra " + str(w1) + " e " + str(w2)
    common_lemmas = len(set(w1.lemma_names).intersection(set(w2.lemma_names)))
    print common_lemmas

def tree (word):
    print ""
    print "Stampa albero di " + str(word)
    hyp = lambda s:s.hypernyms()
    from pprint import pprint
    pprint(word.tree(hyp))
