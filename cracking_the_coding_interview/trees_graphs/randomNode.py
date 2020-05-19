import random

class Node:
	def __init__(self,element):
		self.data = element
		self.right = None
		self.left = None
		self.size = 1

class BST:
	root = None
	noNodes = 0

	def __init__(self):
		self.noNodes = 0

	def addNode(self,root,element):
		self.noNodes += 1
		if(self.root == None):
			self.root = Node(element)
		else:
			root.size += 1
			if root.data < element:
				if root.right is None: 
					root.right = Node(element) 
				else:
					self.addNode(root.right, element)
			else:
				if root.left is None:
					root.left = Node(element) 
				else:
					self.addNode(root.left, element)
	
	def getRoot(self):
		return self.root

	def inOrder(self,root):
		if(root == None):
			return
		self.inOrder(root.left)
		print(root.data)
		self.inOrder(root.right)		
	
	def getRandomNode(self):
		randomIndex = random.randint(1,9)
		print('rand index',randomIndex)
		randomNode = self.calRandomNode(self.root,randomIndex)
		print("Random node",randomNode.data)

	# Gotta restrategize this code easier to write the new code
	def calRandomNode(self,root,ithIndex):
		if(root.left == None or root.right == None):
			left = 0
		else:
			left = root.size
		if(ithIndex < left):
			return self.calRandomNode(root.left,ithIndex)
		elif(ithIndex == left):
			return root
		else:
			return self.calRandomNode(root.right,ithIndex-left)

if __name__ == '__main__':
	obj = BST()
	nodes = [5,4,3,2,1,10,20,30,40]
	for n in nodes:
		obj.addNode(obj.root,n)
	obj.inOrder(obj.root)
	print(obj.root.size)
	obj.getRandomNode()