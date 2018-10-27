"""
Génération aléatoire d'un hypergraphe
un sommet a 1 chance sur 4 d'être un sommet isolé
puis 4 chances sur 10 d'être dans l'hyper-arête dans la boucle "for l in range(len(U)):"
Minimum sommets et 4 hyper-arêtes
"""

from BipartiteGraph import *
from random import randint

def Add_or_not(node, hyp, E):
    """
    Paramètres :
    node: noeud en question (résulte de k in V)
    hyp : hyper-arête en question (U[l])
    E : liste des tupes sommet-hyper arête
    """
    chance = randint(0, 9)
    if chance < 5:
        E.append((hyp, node))

        return E

def generate_Hypergraph():

    _V = randint(3,10) # Calcul du nombre de sommets et hyper-arêtes
    _U = randint(4,7)

    V = ['v' + str(i) for i in range(1, _V +1)]
    U = ['E' + str(j) for j in range(1, _U +1)]

    alone_Summits = [] # Liste des sommets solitaires

    """ Génération de tuples pour creer notre graphe bipartit """
    E = []
    for k in V:
        if randint(0,3) != 0:   # Sinon => sommet solitaire
            finaly = True       # Finalement, est-ce que le sommet à été lié à au moins une hyper-arête
            for l in range(len(U)):
                chance = randint(0, 9)
                if chance < 5:
                    finaly = False
                    E.append((U[l], k))
        if finaly:
            alone_Summits.append(k)

        else:
            alone_Summits.append(k)

    return BipartiteGraph(V, U, E, alone_Summits)
