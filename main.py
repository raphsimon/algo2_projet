from WeightedTree import *
from depthfirst import *
from random import randint
from treeGeneration import *
from tree_Representation_nx import *
from print_tree import *


def main():

    myTree = treeGeneration()
    print("Weight of root: ", myTree.getWeight())
    print("Number of children root has: ", myTree.getNbChildren())
    print("On commence le parcours de l'arbre")
    print()
    print("------------Arbre de Base------------")
    #depthFirst(myTree)
    

    # tree_representation(myTree)
    print_tree(myTree)


    TREE = max_subtree(myTree)
    print()
    print("------------Arbre de Après maximisation------------")
    #depthFirst(TREE)
    

    #tree_representation(TREE)
    print_tree(TREE)

if __name__ == "__main__":
    main()
