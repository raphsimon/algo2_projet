from WeightedTree import *
from depthfirst import *
from random import randint
from treeGeneration import *
from tree_Representation_nx import *
from print_tree import *


def main():

    myTree = treeGeneration()
    myTree2 = treeGeneration()
    print("Weight of root: ", myTree.getWeight())
    print("Number of children root has: ", myTree.getNbChildren())
    print("On commence le parcours de l'arbre")
    print()
    print("------------Arbre de Base------------")


    #tree_representation(myTree)
    #tree_representation(myTree2) # POURQUOI UN MAXIMUM RECURSION ???? WTF



    # first print_tree fonctionne
    print_tree(myTree)


    max_subtree(myTree)
    print()
    print("------------Arbre de Après maximisation------------")

    #tree_representation(myTree)


    print_tree(TREE)

if __name__ == "__main__":
    main()
