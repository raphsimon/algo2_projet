"""
Ceci est l'implémentation d'un graphe primal construit partant
d'un hypergraphe
"""

import networkx as nx

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
            for i in range(1, len(summit_list) - 1):
                # on relie les sommets entre eux
                self.pg.add_edge(summit_list[i-1], summit_list[i])

        self.pg.add_nodes_from(ss) # on ajoute les sommets seuls

    def is_chordal():
        return nx.is_chordal(self.pg)
