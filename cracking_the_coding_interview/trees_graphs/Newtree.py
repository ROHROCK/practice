from ppbtree import *
from random import randint

class NewTree:
	root = None
	def __init__(self):
		self.root = Node()
	
	def addNode(self,listOfNodesToInsert):
		for nodeNumber in listOfNodesToInsert:
			add(self.root, nodeNumber)
	
	def printTree(self):
		print_tree(self.root,left_child='left', right_child='right')