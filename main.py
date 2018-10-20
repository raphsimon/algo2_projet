from WeightedTree import *
from treeGeneration import *
from depthfirst import *
from random import randint


def main():
    myTree = treeGeneration()
    print("Weight of root: ", myTree.getWeight())
    print("Number of children root has: ", len(myTree.getAllChildren()))
    print("On commence le parcours de l'arbre")
    depthFirst(myTree)


if __name__ == "__main__":
    main()
