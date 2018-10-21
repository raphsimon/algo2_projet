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
    nbOfSummits = randint(0, 14) # 14 comme le sommet r est déjà créé
    print("This tree will have ", nbOfSummits, " children(s)")
    addChildrenToTree(summit, nbOfSummits)
    return summit


def addChildrenToTree(summit, childrenToAdd):
    chanceToHaveChildren = randint(1, 4) # le sommet à 1 chance sur 8 d'avoir des fils
    if chanceToHaveChildren != 1: # est-ce que nous allons ajouter des fils?
        if childrenToAdd != 0:
            if childrenToAdd == 1:
                childrenToAddNow = 1
            elif childrenToAdd <= 4: # 4 est le max de fils qu'on peut ajouter
                childrenToAddNow = randint(1, childrenToAdd)
            else:
                childrenToAddNow = randint(1, 4)
            for i in range(childrenToAddNow):
                summit.addChildren(WeightedTree("s", randint(-5, 5), summit))
            childrenToAdd -= childrenToAddNow # pour le prochain appel
            # on parcourt les fils qu'on vient d'ajouter pour en ajouter plus
            childrenToAdd = childrenToAdd // childrenToAddNow
            """ Cette ligne est
            écrite parce que nous aurions à la ligne suivante childrenToAddNow
            fois l'appel récrursif de addChildrenToTree avec chaque fois childrenToAdd
            qui est donné en paramètre ce qui nous donnerait trop d'enfants au final
            """
            for children in range(childrenToAddNow):
                addChildrenToTree(summit.getChildren(children), childrenToAdd)
    return summit
