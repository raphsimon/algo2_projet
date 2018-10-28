import networkx as nx
import matplotlib.pyplot as plt
from random import randint

# def parcours(tree, nbNodes):
#     for i in range(nbNodes):
#         print(tree.nodes[i]['name'], end= " ")
#         print(tree.nodes[i]['weight'])
#         print()

def tree_Generation(nbNodes):
    tree = nx.random_tree(nbNodes)
    node_name = 97                  # lettre 'a'
    tree.nodes[0]['name'] = 'r'
    tree.nodes[0]['weight'] = randint(-5,5)

    for i in range(1, nbNodes):
        tree.nodes[i]['name'] = chr(node_name)
        tree.nodes[i]['weight'] = randint(-5,5)
        node_name += 1

    # nx.draw(tree, with_labels=True)
    # plt.show()

    return tree


# nbNodesChoice = randint(7,15)
# a = tree_Generation(nbNodesChoice)
# parcours(a, nbNodesChoice)

# nx.draw(a, with_labels=True)
# plt.show()
