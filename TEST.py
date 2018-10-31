import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph(name = 'r', weight = 6)
G.add_edge(1,2, weight = 3)


labels = nx.get_edge_attributes(G,'weight')
nx.draw(G, edge_labels=labels, with_labels=True)
plt.show()
