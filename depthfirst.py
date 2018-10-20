"""
Ceci est l'implémentation de l'algorithme de parcours de graphe
en profondeur pour parcourir notre arbre
On utilise cet algorithme parce que l'arbre que nous avons est
un graphe non connexe et les algorithmes pour le parcours d'AB
ne sont pas adaptés à notre structure de données
"""

def depthFirst(sommet):
    # traiter le sommet
    print(sommet.getRootVal())
    # la boucle est la condition d'arret
    for children_i in range(len(sommet.getAllChildren())):
        nextNode = sommet.getChildren(children_i)
        depthFirst(nextNode)
