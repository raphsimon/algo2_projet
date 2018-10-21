from WeightedTree import *
from depthfirst import *
from random import randint
from old_treeGeneration import *


def main():

    myTree = treeGeneration()
    print("Weight of root: ", myTree.getWeight())
    print("Number of children root has: ", myTree.getNbChildren())
    print("On commence le parcours de l'arbre")
    print()
    print("------------Arbre de Base------------")
    depthFirst(myTree)

    max_subtree(myTree)
    print()
    print("------------Arbre de Après maximisation------------")
    depthFirst(myTree)


if __name__ == "__main__":
    main()
