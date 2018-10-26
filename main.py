
from generate_Hypergraph import *
from BipartiteGraph import *
from PrimalGraph import *

import networkx as nx
import matplotlib.pyplot as plt




def main():

    random_Hy_Graph = generate_Hypergraph()

    print(random_Hy_Graph.get_hyper_edges())
    print(random_Hy_Graph.get_solitary_vertices())
    print()
    pg = PrimalGraph(random_Hy_Graph.get_hyper_edges(), random_Hy_Graph.get_solitary_vertices())
    pg.draw()
    print(pg.is_chordal())



if __name__ == '__main__':
    main()
