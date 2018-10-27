"""
Ce ficher contient l'implémentation d'un graphe bipartit.
Nous nous servons de la librairie networkx qui nous facilite
cette tâche (Affichage, implémentation)
"""

import networkx as nx
from networkx.algorithms import bipartite

class BipartiteGraph:
    # U et V sont des listes
    # E est une liste de tuples un tuple cotient un elem de U et de V
    def __init__(self, U, V, E, alone_Summits):
        # U et V sont les deux ensembles de noeuds (Sommets, Hyper-arêtes)
        # E représente les connections entre les deux ensembles de noeuds (liste de tuples (sommet, hyper-arête))
        # les noeuds d'un ensemble ne sont pas reliés entre eux => propriété du graphe biparti

        self.U = U
        self.V = V
        self.alone_Summits = alone_Summits # Sommets isolés
        self.E = E

        self.B = nx.Graph()
        self.B.add_nodes_from(U, bipartite=0) # Distinguer les deux ensembles
        self.B.add_nodes_from(V, bipartite=1)
        self.B.add_edges_from(E)

    def get_top_nodes(self):
        # Retourne la liste des sommets du graphe
        return self.U

    def get_bottom_nodes(self):
        # Retourne la liste des hyper-arêtes du graphe
        return self.V

    def get_edges(self):
        # Retourne la liste des tuples (sommet - hyper-arête) du graphe
        return self.E

    def is_connected(self):
        return nx.is_connected(self.B)

    def get_hyper_edges(self):
        # Création d'un dictionnaire contenant:
        # Clé : Hyper-arête
        # Entrée : liste des sommets qui sont reliés
        # Nous sert à la construction du graphe primal
        hyper_edges = {}
        he = 0      # hyper edge
        n = 1       # node in hyperedge
        for i in range(len(self.E) - 1):
            if self.E[i][he] not in hyper_edges:
                hyper_edges[self.E[i][he]] = [self.E[i][n]]
            else:
                # on ajoute le sommet à l'hyper-arête
                hyper_edges[self.E[i][he]].append(self.E[i][n])
        return hyper_edges

    def get_solitary_vertices(self):
        # retourne une liste avec les sommets qui ne sont pas contenus
        # dans une hyper-arête
        return self.alone_Summits
