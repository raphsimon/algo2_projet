
from generate_Hypergraph import *
from BipartiteGraph import *
from PrimalGraph import *


def is_alphaAcyclic(bool_chordal, max_cliques, hyper_edges):
	res = True
	# pour que l'hypergraphe soit un hypertree il faut satisfaire les
	# 2 conditions (graphe primal er chordal ET alpha-acyclique)
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
	# Ces listes contiennet les sommets contenu dans une hyper-arête
	summit_matrix = []
	for keys in hyper_edges:
		if len(hyper_edges[keys]) >= 2:
			summit_matrix.append(hyper_edges[keys])
	return summit_matrix


def test_hypertree(hg):
	#
	# TO DO : afficher hypergraphe
	#
	hyper_edges = hg.get_hyper_edges()
	solitary_vertices = hg.get_solitary_vertices()
	graphe_primal = PrimalGraph(hyper_edges, solitary_vertices)
	bool_chordal = graphe_primal.is_chordal()
	if bool_chordal:
		max_cliques = graphe_primal.get_max_cliques()
		bool_alphaAcyclic = is_alphaAcyclic(bool_chordal, max_cliques, hyper_edges)
	else:
		bool_alphaAcyclic = False
	return bool_alphaAcyclic


def main():

    random_Hy_Graph = generate_Hypergraph()

    print(random_Hy_Graph.get_hyper_edges())
    print(random_Hy_Graph.get_solitary_vertices())
    print()
    pg = PrimalGraph(random_Hy_Graph.get_hyper_edges(), random_Hy_Graph.get_solitary_vertices())
    max_cliques = pg.get_max_cliques()
    print("Les cliques maximales du graphe: ")
    for cliques in max_cliques:
    	print(cliques)
    pg.draw()
    print(pg.is_chordal())



if __name__ == '__main__':
    main()
