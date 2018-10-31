"""
Génération aléatoire d'un hypergraphe
Minimum 4 sommets et 3 hyper-arêtes
"""

from BipartiteGraph import *
from random import randint

def generate_Hypergraph():

    U = ['v' + str(j) for j in range(1, randint(4,7) +1)] # Sommets
    V = ['E' + str(i) for i in range(1, randint(3,7) +1)] # Hyper-arêtes

    alone_Summits = []      # Liste des sommets solitaires
    alone_Hyp_edges = V[:]  # liste des hyper-arêtes solitaires

    """ Génération de tuples pour creer notre graphe bipartit """
    E = [] # liste des tuples (conexions)
    for u in U: # u dans la liste des Sommets
        finaly = True       # Finalement, est-ce que le sommet à été lié à au moins une hyper-arête
        if randint(0,3) != 0:   # Sinon => sommet solitaire
            for v in V: # V liste des hyper-arêtes
                chance = randint(0, 9)
                if chance < 4:
                    finaly = False
                    E.append((v, u))
                    if v in alone_Hyp_edges:
                        alone_Hyp_edges.remove(v)

                if finaly and v == (len(V)-1):
                    alone_Summits.append(u)
                    if v in alone_Hyp_edges:
                        alone_Hyp_edges.remove(v)

        else:
            alone_Summits.append(u)

    return BipartiteGraph(U, V, E, alone_Summits, alone_Hyp_edges)
