import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

from main import *



""" Graphe de l'énoncé, doit renvoyer True"""

U = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7']
V = ['E1', 'E2', 'E3', 'E4']
E = [('E1', 'v1'), ('E1', 'v2'), ('E2', 'v2'), ('E1', 'v3'), ('E2', 'v3'), ('E3', 'v3'), ('E4', 'v4'), ('E3', 'v5'), ('E3', 'v6')]

graph = BipartiteGraph(U, V, E, ['v7'], [])

print("\n\nHypertree?: ", test_hypertree(graph))
