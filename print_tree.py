
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
	q = Queue()
	q.enqueue(tree)
	while not q.isEmpty():
		s = q.dequeue()
		children = s.getAllChildren()
		if not children:
			print(s.getRootVal(), " : [ ]")
		else:
			string = s.getRootVal() + " : [ "
			for child_i in children:
				string += child_i.getRootVal() + " "
				q.enqueue(child_i)
			string += "]"
			print(string)
