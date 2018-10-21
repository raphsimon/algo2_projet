import networkx as nx
import matplotlib.pyplot as plt
from random import randint


def treeGeneration():
    """
    Cette fonction génère un arbre parmi les règles suivantes:
    - le nombre de sommets est max. 15
    - un sommet peut être de degré 0 à 4
    - chaque sommet aura un poids n: -5 <= n <= 5
    - Il y a une chance de 25% que le sommet reste de degré 0
    """
    summit = nx.Graph(name = "r", weight = randint(-5, 5))
    nbOfSummits = randint(0, 14) # 14 car on retire le sommet qui existe déjà
    print("Number of summits ", nbOfSummits)
    lowercase_a = 97
    addChildrenToTree(summit, nbOfSummits, lowercase_a)
    return summit

def addChildrenToTree(summit, childrenToAdd, node_name):
    print("Entering rec function")
    if childrenToAdd != 0: # cond d'arrêt récursivité
        chanceToHaveChildren = randint(1, 4) # le sommet à 1 chance sur 4 d'avoir des fils
        if chanceToHaveChildren != 1: # allons-nous ajouter des fils?
            if childrenToAdd == 1:
                childrenToAddNow = 1 # init compteur de bloucle
            elif childrenToAdd <= 4:
                childrenToAddNow = randint(1, childrenToAdd)
            else: # Si on a encore plus que 4 fils à ajouter
                childrenToAddNow = randint(1, 4)
            for children in range(childrenToAddNow):
                temp = nx.Graph(name = chr(node_name), weight = randint(-5, 5))
                node_name += 1 # pour nommer le prochain noeud autrement
                summit.add_node(temp)
                summit.add_edge(G, temp)
            childrenToAdd -= childrenToAddNow
            nb_children_next = childrenToAdd // childrenToAddNow
            # Cette ligne est ajouté pour ne pas faire n appel récursif avec
            # le childrenToAdd enfants car l'arbre aura trop de fils
            summit_nodes = list(summit.nodes()) # les noeuds qu'on vient d'ajouter
            for node in summit_nodes:
                addChildrenToTree(node, nb_children_next, node_name)
    return summit