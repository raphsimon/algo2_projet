"""
Date: 12.11.18
Authors:
Mangriotis Aris	: 	000460001
Simon Raphael 	: 	000462263

Projet: Algorithmique
"""

class WeightedTree:
    """
    Ceci est l'implémentation de l'ADT pour résoudre le problème
    du sous-arbre de poids maximum
    """
    def __init__(self, rootVal, weight, father):
        self.key = rootVal      # Id du sommet (lettre)
        self.father = father    # Pour remonter dans l'arbre
        self.weight = weight    # Poids associé au noeud
        self.childrenList = []  # Pas d'enfants par défaut
        self.nbChildren = 0     # Nombre d'enfants
        self.potential = weight # Somme du sommet avec les sommes des enfants

    def getRootVal(self):
        return self.key

    def setPotential(self, value):
        self.potential += value

    def getPotential(self):
        return self.potential

    def getFather(self):
        return self.father

    def getWeight(self):
        return self.weight

    def getChildren(self, childNb):
        # Renvoie un enfant en particulier
        try:
            return self.childrenList[childNb]
        except IndexError:
            print("Pas un argument valide!")

    def getAllChildren(self):
        # Renvoie la liste des enfants
        return self.childrenList

    def getNbChildren(self):
        # Renvoie le nombre d'enfants
        return self.nbChildren

    def setChildren(self, newChild, newChildIndex):
        # On modifie un enfant déjà existant
        try:
            self.childrenList[newChildIndex] = newChild
        except IndexError:
            print("Pas un argument valide!")

    def addChildren(self, newChild):
        # ajout d'un enfant dans la liste des enfants
        self.childrenList.append(newChild)
        self.nbChildren += 1

    def deleteChild(self, child):
        self.childrenList[self.childrenList.index(child)] = None
        self.nbChildren -= 1

    def deleteAllChildren(self):
        self.childrenList = []
        self.nbChildren = 0
