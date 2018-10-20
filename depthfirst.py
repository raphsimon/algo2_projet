
"""
Ceci est l'implémentation de l'algorithme de parcours de graphe
en profondeur.
On utilise cet algorithme parce que l'arbre que nous avons est
un graphe non connexe et les algorithmes pour le parcours d'AB
ne sont pas adaptés à notre structure de données
"""

def depthFirst(summit):
    # traiter le sommet
    # print(summit.getRootVal())

    # la boucle est la condition d'arrêt
    for child_i in range(summit.getNbChildren()):
        nextNode = summit.getChildren(child_i)
        depthFirst(nextNode)

    if summit.getNbChildren() == 0:     # Si le sommet rencontré est une feuille
        if summit.getRootVal() <= 0:    # Si la feuille est de poids négatif ou 0
            # Delete la feuille #Bug pour le prochain child_i car décale d'index les enfants suivants!
            # summit.getFather.deleteChildren(*paramètre* (self?))
        else:
            # Contribution positive -> mettre à jour le potentiel du père
            summit.getFather.setPotentiel(summit.getRootVal())
    else:
    """Noeud interne -> Nous somme maintenant sûrs que les enfants ont un poids positif
    Les feuilles à poids négatif ont été supprimées juste avant"""

        if summit.getPotentiel() > 0:
            """On verifie si les poids des enfants ont suffit pour que tout
            le sous arbre ait un poids positif, sinon on supprime tout le sous arbre"""
            summit.getFather.setPotentiel(summit.getPotentiel())
        else:
            # Delete le sommet (et indirectement tous les sous arbres)



def maximise(summit):
    pass
