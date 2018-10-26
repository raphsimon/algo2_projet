from WeightedTree import *

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
    neighbors = list(G.nodes)
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




def tree_creation(tree_base):
    """Création de l'Arbre sous Networkx"""
    G = nx.Graph(name = tree_base.getRootVal(), weight = tree_base.getWeight())
    for i in range(len(tree_base.getAllChildren())):
        if tree_base.getChildren(i) != None:
            G.add_edge(G,tree_creation(tree_base.getChildren(i)), weight = tree_base.getChildren(i).getWeight())
    return G







def tree_show(G):
    """Affichage de l'arbre"""
    nx.draw(G, pos=nx.circular_layout(G), with_labels=True)
    labels = nx.get_edge_attributes(G,'weight')
    #nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels=labels)
    nx.draw_networkx_edge_labels(G, pos=hierarchy_pos(G, 0), edge_labels=labels)
    plt.show()

    # tree_show(G)
    # plt.show()





#
# def tree_creation(tree_target, tree_base):
#     """Création de l'Arbre sous Networkx"""
#     for i in range(len(tree_base.getAllChildren())):
#         if tree_base.getChildren(i) != None:
#             tree_target.add_node(tree_base.getChildren(i), weight = tree_base.getChildren(i).getWeight())
#             #tree_target.add_edge(tree_target, )
#             #tree_creation(tree_base.getChildren(i)), weight = tree_base.getChildren(i).getWeight())
#
#
#     return tree_target
#
#


def tree_representation(tree):
    #nx.draw(G, pos=hierarchy_pos(G, 0), with_labels=True)
    #G = nx.Graph(name = tree.getRootVal(), weight = tree.getWeight())
    #G = tree_creation(nx.Graph(name = tree.getRootVal(), weight = tree.getWeight()), tree)
    G = tree_creation(tree)
    #print(list(G.nodes))
    tree_show(G)










# #!/usr/bin/python
# import networkx as nx
# import matplotlib.pyplot as plt
#
# G=nx.Graph()
# i=1
# G.add_node(i,pos=(i,i))
# G.add_node(2,pos=(2,2))
# G.add_node(3,pos=(1,0))
# G.add_edge(1,2,weight=0.5)
# G.add_edge(1,3,weight=9.8)
# pos=nx.get_node_attributes(G,'pos')
# nx.draw(G,pos)
# labels = nx.get_edge_attributes(G,'weight')
# nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
# plt.savefig(<wherever>)
