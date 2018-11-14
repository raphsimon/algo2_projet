"""
Date: 12.11.18
Authors:
Mangriotis Aris	: 	000460001
Simon Raphael 	: 	000462263

Projet: Algorithmique

Génération aléatoire d'un hypergraphe
Minimum 4 sommets et 3 hyper-arêtes
"""

from BipartiteGraph import *
from random import randint

def generate_Hypergraph():

    V = ['v' + str(j) for j in range(1, randint(4,7) +1)] # Sommets
    E = ['E' + str(i) for i in range(1, randint(3,7) +1)] # Hyper-arêtes

    alone_Summits = []      # Liste des sommets solitaires
    alone_Hyp_edges = E[:]  # liste des hyper-arêtes solitaires

    """ Génération de tuples pour creer notre graphe bipartit """
    C = [] # liste des tuples (conexions)
    for v in V: # v dans la liste des Sommets
        finaly = True       # Finalement, est-ce que le sommet à été lié à au moins une hyper-arête
        if randint(0,3) != 0:   # Sinon => sommet solitaire
            for e in E: # E liste des hyper-arêtes
                chance = randint(0, 9)
                if chance < 4:
                    finaly = False
                    C.append((e, v))

                if finaly and e == (len(E)-1):
                    alone_Summits.append(v) # Le sommet est finalement solitaire

                if e in alone_Hyp_edges:
                    alone_Hyp_edges.remove(e) # Hper-arête reliée -> N'est plus seule
        else:
            alone_Summits.append(v)

    return BipartiteGraph(V, E, C, alone_Summits, alone_Hyp_edges)
