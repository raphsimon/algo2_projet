"""
Mangriotis Aris	: 	000460001
Simon Raphael 	: 	000462263
"""


from WeightedTree import *
from depthfirst import *
from random import randint
from treeGeneration import *
from print_tree import *


def main():

    myTree = treeGeneration()
    myTree2 = treeGeneration()
    print("Weight of root: ", myTree.getWeight())
    print("Number of children root has: ", myTree.getNbChildren())
    print("On commence le parcours de l'arbre")
    print()
    print("------------Arbre de Base------------")


    # first print_tree
    print_tree(myTree)

	# MAXIMISATION DE L'ARBRE
    max_subtree(myTree)

    print("\n\n------------Arbre de Après maximisation------------")

	# second print_tree after maximisation
    print_tree(myTree)



if __name__ == "__main__":
    main()
