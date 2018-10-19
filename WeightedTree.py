class WeightedTree:
    """
    Ceci est l'implémentation de l'ADT pour résoudre le problème
    du sous-arbre de poids maximum
    """
    def __init__(self, rootVal, weight, father=None):
        self.key = rootVal
        self.father = father # Pour remonter dans l'arbre
        self.weight = weight # Poids associé au noeud
        self.childrenList = [] # Pas d'enfants par défaut

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
