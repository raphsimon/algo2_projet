
"""
Ceci est l'implémentation de l'algorithme de parcours de graphe
en profondeur.
On utilise cet algorithme parce que l'arbre que nous avons est
un graphe non connexe et les algorithmes pour le parcours d'AB
ne sont pas adaptés à notre structure de données
"""

def depthFirst(summit):
    # traiter le summit
    print(summit.getRootVal())

    # la boucle est la condition d'arrêt
    for child_i in range(summit.getNbChildren()):
        nextNode = summit.getChildren(child_i)
        depthFirst(nextNode)

    if summit.getNbChildren() == 0:  # Si le sommet est une feuille
        if summit.getRootVal() < 0: # Si la feuille est de poids négatif
            # Delete la feuille
            # summit.getFather.deleteChildren(?)
        else:
            # Contribution positive -> mettre à jour le potentiel du père
            summit.getFather.setPotentiel(summit.getRootVal())
    else:
        #summit.
        maximise(summit)



def maximise(summit):
    pass
