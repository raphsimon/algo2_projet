
"""
Ceci est l'implémentation de l'algorithme de parcours de graphe
en profondeur.
On utilise cet algorithme parce que l'arbre que nous avons est
un graphe non connexe et les algorithmes pour le parcours d'AB
ne sont pas adaptés à notre structure de données
"""

def depthFirst(summit):

    if summit != None:
        print(summit.getRootVal())

        for child_i in range(summit.getNbChildren()):
            nextNode = summit.getChildren(child_i)
            depthFirst(nextNode)




def max_subtree(summit):
    # traiter le sommet
    # print(summit.getRootVal())

    # la boucle est la condition d'arrêt
    for child_i in range(summit.getNbChildren()):
        nextNode = summit.getChildren(child_i)
        max_subtree(nextNode)

    if summit.getRootVal() != "r":
        if summit.getNbChildren() == 0:     # Si le sommet rencontré est une feuille
            if summit.getWeight() <= 0:     # Si la feuille est de poids négatif ou égale 0
                # Suppression de la feuille
                summit.getFather().deleteChild(summit)
            else:
                # Contribution positive -> mettre à jour le potentiel du père
                summit.getFather().setPotential(summit.getWeight())
        else:
            """Noeud interne -> Nous somme maintenant sûrs que les enfants ont un poids positif
            Les feuilles à poids négatif ont été supprimées juste avant"""

            if summit.getPotential() > 0 : #and summit.getRootVal() != "r":
                """On verifie si les poids des enfants ont suffit pour que tout
                le sous arbre ait un poids positif, sinon on supprime tout le sous arbre"""
                summit.getFather().setPotential(summit.getPotential())
            else:
                # Suppression du noeud interne
                summit.getFather().deleteChild(summit)
