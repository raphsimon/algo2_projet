"""
Date: 12.11.18
Authors:
Mangriotis Aris	: 	000460001
Simon Raphael 	: 	000462263

Projet: Algorithmique

Ce ficher contient l'implémentation d'un graphe bipartit.
Nous nous servons de la librairie networkx qui nous facilite
cette tâche (Affichage, implémentation)
"""

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

class BipartiteGraph:
    # summits et Hyp_edges sont des listes
    # conexions est une liste de tuples un tuple cotient un elem de summits et de Hyp_edges
    def __init__(self, summits, Hyp_edges, conexions, alone_Summits, alone_Hyp_edges):
        # summits et Hyp_edges sont les deux ensembles de noeuds (Sommets, Hyper-arêtes)
        # conexions représente les connections entre les deux ensembles de noeuds (liste de tuples (sommet, hyper-arête))
        # les noeuds d'un ensemble ne sont pas reliés entre eux => propriété du graphe biparti
        self.summits = summits # Sommets
        self.Hyp_edges = Hyp_edges # Hyper-arêtes
        self.alone_Summits = alone_Summits # Sommets isolés
        self.alone_Hyp_edges = alone_Hyp_edges
        self.conexions = conexions
        self.B = nx.Graph()
        self.B.add_nodes_from(summits, bipartite=0) # Distinguer les deux ensembles
        self.B.add_nodes_from(Hyp_edges, bipartite=1)
        self.B.add_edges_from(conexions)
        self.colors = ['r' for i in range(len(summits))] + ['g' for j in range(len(Hyp_edges))]

    def get_top_nodes(self):
        # Retourne la liste des sommets du graphe
        return self.summits

    def get_bottom_nodes(self):
        # Retourne la liste des hyper-arêtes du graphe
        return self.Hyp_edges

    def get_edges(self):
        # Retourne la liste des tuples (sommet - hyper-arête) du graphe
        return self.conexions

    def is_connected(self):
        return nx.is_connected(self.B)

    def get_hyper_edges(self):
        # Création d'un dictionnaire contenant:
        # Clé : Hyper-arête
        # Entrée : liste des sommets qui sont inclus dans l'hyper-arête
        # Nous sert à la construction du graphe primal
        hyper_edges = {}
        he = 0      # hyper edge
        n = 1       # node in hyperedge
        for i in range(len(self.conexions)):
            if self.conexions[i][he] not in hyper_edges:
                hyper_edges[self.conexions[i][he]] = [self.conexions[i][n]]
            else:
                # on ajoute le sommet à l'hyper-arête
                hyper_edges[self.conexions[i][he]].append(self.conexions[i][n])
        return hyper_edges

    def get_solitary_vertices(self):
        # retourne une liste avec les sommets qui ne sont pas contenus
        # dans une hyper-arête
        return self.alone_Summits

    def to_Dual(self):
        # Retourne l'hypergraphe Dual (inversé)
        return BipartiteGraph(self.Hyp_edges, ['E' + i for i in self.summits],
        [tuple(reversed((x[0], 'E'+x[1]))) for x in self.conexions], self.alone_Hyp_edges, ['E' + j for j in self.alone_Summits])
        #return BipartiteGraph(self.Hyp_edges, self.summits, [tuple(reversed(x) for x in self.conexions], self.alone_Hyp_edges, self.alone_Summits)

    def draw(self):
        # Représentation en graphe biparti
        X = self.summits
        Y = self.Hyp_edges
        pos = dict()
        pos.update( (j, (1, i)) for i, j in enumerate(X) ) # position
        pos.update( (j, (2, i)) for i, j in enumerate(Y) )
        plt.figure("Dual HyperGraph")
        nx.draw(self.B, node_color = self.colors, pos=pos, with_labels = True)
        plt.show()
