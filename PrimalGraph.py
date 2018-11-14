"""
Date: 12.11.18
Authors:
Mangriotis Aris	: 	000460001
Simon Raphael 	: 	000462263

Projet: Algorithmique

Ceci est l'implémentation d'un graphe primal construit partant
d'un hypergraphe
"""

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.clique import find_cliques


class PrimalGraph:
    # hyper_aretes est un dictionaire
    # keys : hyper-arêtes
    # values : liste contenant les sommets contenu dans l'hyper-arête
    def __init__(self, hyper_aretes, sommets_seuls):
        self.pg = nx.Graph()
        self.build_PrimalGraph(hyper_aretes, sommets_seuls)

    def build_PrimalGraph(self, ha, ss):
        for keys in ha:
            summit_list = ha[keys]
            self.pg.add_nodes_from(summit_list)
            """
            networkx va ajouter chacun des noeuds qu'une seule fois.
            Si le noeud est déjà contenu dans le graphe, on ne rajoute
            plus
            """
            for i in range(1, len(summit_list)):
                # on relie les sommets entre eux
                # print("On relie ", summit_list[i-1], "et ", summit_list[i])
                self.pg.add_edge(summit_list[i-1], summit_list[i])
            # on relie le premier et le dernier
            if len(summit_list) > 1: # Evite les auto-boucles
                self.pg.add_edge(summit_list[0], summit_list[-1])
        self.pg.add_nodes_from(ss) # on ajoute les sommets seuls

    def is_chordal(self):
        return nx.is_chordal(self.pg)

    def draw(self):
        plt.figure("Primal Graph")
        nx.draw(self.pg, with_labels=True)
        plt.show()

    def get_max_cliques(self):
        # retourne un iterateur sur les cliques maximales du graphe primal
        return find_cliques(self.pg)
