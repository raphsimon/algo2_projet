
class Queue:
	"""
	Simple queue implementation using python lists
	"""
	def __init__(self):
	    self.items = []

	def isEmpty(self):
	    return not self.items

	def enqueue(self, item):
	    self.items.insert(0,item)

	def dequeue(self):
	    return self.items.pop()

	def size(self):
	    return len(self.items)


def print_tree(tree):
	"""
	tree: WeightedTree object
	We use the breadth first algorithm to print out te children.
	The function wil print out the tree in form of lists of successors.
	Where the successors are the children of a node. Here we the
	successors will only be children one level lower than the parent
	"""
	try:
		tree == []
		print("r : []")
		print("Pas de sous arbre maximal pour cet arbre!")
	except:
		q = Queue()
		q.enqueue(tree)
		while not q.isEmpty():
			s = q.dequeue()
			children = s.getAllChildren()
			if (not children) or (len(children) == 1 and None in children):
				string = s.getRootVal() + "(" + str(s.getWeight()) + ") : [ ]"
				print(string)
			else:
				string = s.getRootVal() + "(" + str(s.getWeight()) + ") : ["
				for child_i in children:
					if child_i != None: # Cette condition est ajouté pour faire le
					# print après le maximiser
						string += child_i.getRootVal() + "(" + str(child_i.getWeight()) + "); "
						q.enqueue(child_i)
				string = string[0: -2] # on enlève la virgule en trop
				string += "]"
				print(string)
