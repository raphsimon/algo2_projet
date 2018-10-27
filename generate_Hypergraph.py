"""
Génération aléatoire d'un hypergraphe
un sommet a 1 chance sur 4 d'être un sommet isolé
puis 4 chances sur 10 d'être dans l'hyper-arête dans la boucle "for l in range(len(U)):"
Minimum sommets et 4 hyper-arêtes
"""


from BipartiteGraph import *
from random import randint

def Add_or_not(node, hyp, E):
    chance = randint(0, 9)
    if chance < 5:
        E.append((hyp, node))

        return E

def generate_Hypergraph():
    # On se sert des graphes d'incidence pour générer l'hypergraphe
    _V = randint(3,10)
    _U = randint(4,7)

    V = ['v' + str(i) for i in range(1, _V +1)]
    U = ['E' + str(j) for j in range(1, _U +1)]

    alone_Summits = [] # Liste des sommets solitaires

    """ Génération de tuples pour creer notre graphe bipartit """
    E = []
    for k in V:
        if randint(0,3) != 0:           # Sinon => sommet solitaire
            for l in range(len(U)):
                Add_or_not(k, U[l], E)  # BUG: si Add_or_not n'ajoute jamais -> aussi sommet solitaire !
        else:
            alone_Summits.append(k)

    return BipartiteGraph(V, U, E, alone_Summits)
