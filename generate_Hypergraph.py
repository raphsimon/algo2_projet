"""
Génération aléatoire d'un hypergraphe
Minimum 4 sommets et 3 hyper-arêtes
"""

from BipartiteGraph import *
from random import randint

def generate_Hypergraph():

    _U = randint(4,7) # Sommets
    _V = randint(3,10) # hyper-arêtes
    # On se sert des graphes d'incidence pour générer l'hypergraphe

    U = ['v' + str(j) for j in range(1, _U +1)]
    V = ['E' + str(i) for i in range(1, _V +1)]

    alone_Summits = [] # Liste des sommets solitaires

    """ Génération de tuples pour creer notre graphe bipartit """
    E = []
    for k in U: # k dans la liste des Sommets
        finaly = True       # Finalement, est-ce que le sommet à été lié à au moins une hyper-arête
        if randint(0,3) != 0:   # Sinon => sommet solitaire
            for l in range(len(V)): # V liste des hyper-arêtes
                chance = randint(0, 9)
                if chance < 4:
                    finaly = False
                    E.append((V[l], k))
        if finaly:
            alone_Summits.append(k)

        else:
            alone_Summits.append(k)

    return BipartiteGraph(U, V, E, alone_Summits)
