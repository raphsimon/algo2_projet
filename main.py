
from generate_Hypergraph import *
from BipartiteGraph import *
from PrimalGraph import *


def max_cliques(max_cliques, hyper_edges):   # BUG: Verifier si c'est juste !!!
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

	hg.draw()
	primal_graph = PrimalGraph(hg.get_hyper_edges(), hg.get_solitary_vertices())
	primal_graph.draw()

	hgd = hg.to_Dual()
	hgd.draw()
	graphe_primal = PrimalGraph(hgd.get_hyper_edges(), hgd.get_solitary_vertices())
	graphe_primal.draw()

	return graphe_primal.is_chordal() and max_cliques(graphe_primal.get_max_cliques(), hg.get_hyper_edges())


def main():

	random_Hy_Graph = generate_Hypergraph()
	#print("Sommets dans les Hyper-arêtes: ", random_Hy_Graph.get_hyper_edges())
	#print("Sommets seuls: ", random_Hy_Graph.get_solitary_vertices())
	#print("Conexions: ", random_Hy_Graph.get_edges())

	print("\n\nHyperTree ?: ", test_hypertree(random_Hy_Graph))


if __name__ == '__main__':
    main()
