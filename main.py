
from generate_Hypergraph import *
from BipartiteGraph import *
from PrimalGraph import *


def is_alphaAcyclic(bool_chordal, max_cliques, hyper_edges):
	res = True
	# pour que l'hypergraphe soit un hypertree il faut satisfaire les
	# 2 conditions (graphe primal chordal ET alpha-acyclique)
	he_summits = get_he_summits(hyper_edges)
	for cliques in max_cliques:
		# on sort pour que le IN fonctionne car les sommets dans
		# max_cliques ne sont pas triées
		if cliques.sort() not in he_summits:
			res = False
	return res

def get_he_summits(hyper_edges):
	# hyper_edges : type dictionary
	# Cette fonction retourne une liste contenant des listes.
	# Ces listes contiennent les sommets contenu dans une hyper-arête
	summit_matrix = []
	for keys in hyper_edges:
		if len(hyper_edges[keys]) >= 2:
			# Clique de taille 2 ou plus
			summit_matrix.append(hyper_edges[keys])

	return summit_matrix


def test_hypertree(hg):
	#
	# TO DO : afficher hypergraphe
	#
	hg.draw()
	hyper_edges = hg.get_hyper_edges()
	graphe_primal = PrimalGraph(hyper_edges, hg.get_solitary_vertices())
	graphe_primal.draw()
	bool_chordal = graphe_primal.is_chordal()

	return bool_chordal and is_alphaAcyclic(bool_chordal, graphe_primal.get_max_cliques(), hyper_edges)


def main():

    random_Hy_Graph = generate_Hypergraph()

    print("Sommets dans les Hyper-arêtes: ", random_Hy_Graph.get_hyper_edges())
    print("Sommets seuls: ", random_Hy_Graph.get_solitary_vertices())
    print()
    print(test_hypertree(random_Hy_Graph))



if __name__ == '__main__':
    main()
