from WeightedTree import *
from new_depthfirst import *
# from Random_tree import *
from random import randint
from treeGeneration import *
from depthfirst import *


def main():

    # my_tree = tree_Generation(randint(7,15))
    # max_subtree(my_tree)


    myTree = treeGeneration()
    print("Weight of root: ", myTree.getWeight())
    print("Number of children root has: ", len(myTree.getAllChildren()))
    print("On commence le parcours de l'arbre")
    depthFirst(myTree)


if __name__ == "__main__":
    main()
