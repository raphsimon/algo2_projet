"""
Ce ficher contient l'implémentation d'un graphe bipartite
nous nous servons de la librairie networkx qui nous facilite
cette tâche
"""

import networkx as nx
from networkx.algorithms import bipartite

class BipartiteGraph:
    # U et V sont des listes
    # E est une liste de tuples un tuple cotient un elem de U et de V
    def __init__(self, U, V, E):
        # U et V sont les deux ensembles de noeuds
        # E représente les connections entre les deux ens de noeuds
        # les noeuds d'un ens ne sont pas reliés entre eux
        self.U = U
        self.V = V
        self.E = E
        self.B = nx.Graph()
        self.B.add_nodes_from(U, bipartite=0)
        self.B.add_nodes_from(V, bipartite=1)
        self.B.add_edges_from(E)

    def get_top_nodes(self):
        return self.U
    
    def get_bottom_nodes(self):
        return self.V
    
    def get_edges(self):
        return self.E

    def is_connected(self):
        return nx.is_connected(self.B)

    def get_hyper_edges(self):
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

    def get_solitary_vertives():
        # retourne une liste avec les sommets qui ne sont pas contenus
        # dans une hyper-arête
        pass
