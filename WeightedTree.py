import random

class WeightedTree:
    """
    Ceci est l'implémentation de l'ADT pour résoudre le problème
    du sous-arbre de poids maximum
    """
    def __init__(self, rootVal, weight, MAX, ID=1, father=None):
        self.key = rootVal
        self.father = father # Pour remonter dans l'arbre
        self.weight = weight # Poids associé au noeud
        if MAX < 15:
            if random.randint(0,1) != 0:
                self.childrenList = [WeightedTree(ROOTVAL, random.randint(-5,5), self) for _ in range(random.randint(1,4))]
            else:
                self.childrenList = []

    def getRootVal(self):
        return self.key

    def setRootVal(self, key):
        self.key = key

    def getFather(self):
        return self.father

    def setFather(self, newFather):
        self.father = newFather

    def getWeight(self):
        return self.weight

    def setWeight(self, newWeight):
        self.weight = newWeight

    def getChildren(self, childrenNb):
        try:
            return childrenList[childrenNb]
        except IndexError:
            print("Pas un argument valide!")

    def getAllChildren(self):
        return self.childrenList

    def setChildren(self, newChild, newChildIndex):
        # On modifie un enfant déjà existant
        try:
            self.childrenList[newChildIndex] = newChild
        except IndexError:
            print("Pas un argument valide!")

    def addChildren(self, newChild):
        # ajout d'enfant dans la liste enfants
        self.childrenList.append(newChild)
