
from random import randint

def generate_Hypergraph():

    _1 = randint(3,10)
    _2 = randint(4,7)

    V = ['v' + str(i) for i in range(1,_1+1)]
    U = ['E' + str(j) for j in range(1,_2+1)]


    E = list()
    for k in V:
        for l in range(len(U)):
            Add_or_not(k, U[l], E)


    return V, U, E



def Add_or_not(node, hyp, E):
    chance = randint(0, 9) # 1 chance sur 4 d'être dans l'hyper-arête
    if chance < 5:
        E.append((hyp, node))

    return E
