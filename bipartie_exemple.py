import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

V = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7']
E = ['E1', 'E2', 'E3', 'E4']
arcs = [('v1', 'E1'), ('v2', 'E1'), ('v2', 'E2'), ('v3', 'E1'), ('v3', 'E2'), ('v3', 'E3'), ('v4', 'E4'), ('v5', 'E3'), ('v6', 'E3')]

B = nx.Graph()
# ajout de noeuds avec l'attribut "bipartite"
B.add_nodes_from(V, bipartite=0) # 0 ou 1 spécifient dans quelle région on ajoute
B.add_nodes_from(E, bipartite=1) # les noeuds
# add edges only between nodes of opposite set
B.add_edges_from(arcs)

print(nx.is_connected(B))
if nx.is_connected(B):
    bottom_nodes, top_nodes = bipartite.sets(B)
    print("Bottom nodes: ", bottom_nodes)
    print("Top nodes: ", top_nodes)
else:
    # We need to use another method to get the two node sets
    """
    this somehow doesn't work, I think i need to add a bipartite argument to the node
    top_nodes = {n for n, d in B.nodes(data=True) if d['bipartite']==0}
    bottom_nodes = set(B) - top_nodes
    print("Bottom nodes: ", bottom_nodes)
    print("Top nodes: ", top_nodes)
    """
    print("Not connected")


nx.draw(B, with_labels=True)
plt.show()
