"""
Mangriotis Aris	: 	000460001
Simon Raphael 	: 	000462263
"""

from WeightedTree import *
from random import randint

# returns a tree
def treeGeneration():
    """
    Cette fonction génère un arbre parmi les règles suivantes:
    - le nombre de sommets est max. 15
    - un sommet peut être de degré 0 à 4
    - chaque sommet aura un poids n: -5 <= n <= 5
    - Il y a une chance de 25% que le sommet reste de degré 0
    """
    summit = WeightedTree("r", randint(-5, 5), None)
    nbOfSummits = randint(7, 14) # 14 comme le sommet r est déjà créé
    node_name = 97 # identifiant: lettre du sommet (97 -> lettre a )
    print("This tree will have ", nbOfSummits, " children(s)")
    addChildrenToTree(summit, nbOfSummits, node_name)
    return summit


def addChildrenToTree(summit, childrenToAdd, node_name):
    # chanceToHaveChildren = randint(1, 4) # le sommet à 1 chance sur 4 d'avoir des fils
    # if chanceToHaveChildren != 1: # est-ce que nous allons ajouter des fils?
    if childrenToAdd != 0:
        if childrenToAdd == 1:
            childrenToAddNow = 1
        elif childrenToAdd <= 4: # 4 est le max de fils qu'on peut ajouter
            childrenToAddNow = randint(1, childrenToAdd)
        else:
            childrenToAddNow = randint(1, 4)
        for i in range(childrenToAddNow):
            #print(childrenToAddNow)
            summit.addChildren(WeightedTree(chr(node_name), randint(-5, 5), summit))
            node_name += 1
        childrenToAdd -= childrenToAddNow
        # childrenToAdd = reste pour le prochain appel

        liste = distribution(childrenToAddNow, childrenToAdd)
        i = 0
        for child_i in range(childrenToAddNow):
            addChildrenToTree(summit.getChildren(child_i), liste[child_i], node_name)
            node_name +=  liste[child_i]
    return summit



def distribution(nbSummits, childrenToAdd):
    # Distibue le nombre de fils à rajouter à chaque noeud
    liste = list()
    rest = 0
    for i in range(nbSummits):
        res = randint(0, childrenToAdd-rest)
        liste.append(res)
        rest += res

    liste[-1] += (childrenToAdd-sum(liste))

    return liste
