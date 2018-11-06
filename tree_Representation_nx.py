from WeightedTree import *
from depthfirst import*

import networkx as nx
import matplotlib.pyplot as plt

def hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5,
                  pos = None, parent = None):
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node of current branch
       width: horizontal space allocated for this branch - avoids overlap with other branches
       vert_gap: gap between levels of hierarchy
       vert_loc: vertical location of root
       xcenter: horizontal location of root
       pos: a dict saying where all nodes go if they have been assigned
       parent: parent of this branch.'''
    if pos == None:
        pos = {root:(xcenter,vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    neighbors = list(G.neighbors(root))
    if parent != None:   #this should be removed for directed graphs.
        neighbors.remove(parent)  #if directed, then parent not in neighbors.
    if len(neighbors)!=0:
        dx = width/len(neighbors)
        nextx = xcenter - width/2 - dx/2
        for neighbor in neighbors:
            nextx += dx
            pos = hierarchy_pos(G,neighbor, width = dx, vert_gap = vert_gap,
                                vert_loc = vert_loc-vert_gap, xcenter=nextx, pos=pos,
                                parent = root)
    return pos



def tree_show(G):
    """Affichage de l'arbre"""
    #nx.draw(G, pos=nx.circular_layout(G), with_labels=True)
    #nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels=labels)

    labels = nx.get_edge_attributes(G,'weight')
    print(labels)
    nx.draw(G, pos = hierarchy_pos(G, 'r'), edge_labels=labels, with_labels=True)
    plt.show()


def tree_creation(tree_base, G = nx.Graph()):

    for i in tree_base.getAllChildren():
        if i != None:
            G.add_edge(tree_base.getRootVal(), i.getRootVal(), weight = i.getWeight())
            tree_creation(i, G)

    return G

def tree_representation(tree):
    #nx.draw(G, pos=hierarchy_pos(G, 0), with_labels=True)
    #G = nx.Graph(name = tree.getRootVal(), weight = tree.getWeight())
    #G = tree_creation(nx.Graph(name = tree.getRootVal(), weight = tree.getWeight()), tree)
    depthFirst(tree)
    G = tree_creation(tree)
    tree_show(G)
