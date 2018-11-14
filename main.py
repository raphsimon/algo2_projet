"""
Date: 12.11.18
Authors:
Mangriotis Aris	: 	000460001
Simon Raphael 	: 	000462263

Projet: Algorithmique
"""

#from WeightedTree import *
from max_subtree import *
from treeGeneration import *
from print_tree import *
from main_hypertree import *
from random import randint


def main():
    random_Tree = treeGeneration()
    print("\n---------------Arbre avant la maximisation------------\n")
    print_tree(random_Tree)
    print()
    max_subtree(random_Tree)
    print("\n---------------Arbre de Après maximisation------------\n")
    print_tree(random_Tree)
    print()


if __name__ == "__main__":
    main()
    main_hypertree()
