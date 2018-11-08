from generate_Hypergraph import *
from BipartiteGraph import *
from PrimalGraph import *


def max_cliques(max_cliques, he_summits):

	res = True
	# pour que l'hypergraphe soit un hypertree il faut satisfaire les
	# 2 conditions (graphe primal chordal ET alpha-acyclique)
	for cliques in max_cliques:
		if len(cliques) >= 2: # de taille 2 ou plus
			pos = 0
			for i in cliques:
				cliques[pos] = 'v'+ i[1]
				# On change le nom car à l'affichage ce sont des sommets qui s'apellent "E" et non 'v'
				# Vu que l'on a permuté les ensembles
				pos += 1
			# on sort pour que le IN fonctionne car les sommets dans
			# max_cliques ne sont pas triées
			cliques.sort()
			if  cliques not in he_summits:
				res = False
	return res



def get_he_summits(hyper_edges):
	# hyper_edges : type dictionary
	# Cette fonction retourne une liste contenant des listes.
	# Ces listes contiennent les sommets contenu dans une hyper-arête
	summit_sets = []
	for keys in hyper_edges:
		summit_sets.append(hyper_edges[keys])

	return summit_sets



def test_hypertree(hg):

	# hg.draw()
	# primal_graph = PrimalGraph(hg.get_hyper_edges(), hg.get_solitary_vertices())
	# primal_graph.draw()

	hgd = hg.to_Dual()
	hgd.draw()
	graphe_primal = PrimalGraph(hgd.get_hyper_edges(), hgd.get_solitary_vertices())
	# graphe_primal.draw()

	# get_max_cliques est un méthode de Networkx
	print(graphe_primal.is_chordal())
	return graphe_primal.is_chordal() and max_cliques(graphe_primal.get_max_cliques(), get_he_summits(hg.get_hyper_edges()))


def main():

	random_Hy_Graph = generate_Hypergraph()
	#print("Sommets dans les Hyper-arêtes: ", random_Hy_Graph.get_hyper_edges())
	#print("Sommets seuls: ", random_Hy_Graph.get_solitary_vertices())
	#print("Conexions: ", random_Hy_Graph.get_edges())
	print("\n\nHyperTree ?: ", test_hypertree(random_Hy_Graph))


if __name__ == '__main__':
    main()
