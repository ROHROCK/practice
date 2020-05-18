import random

class Node:
	def __init__(self,element):
		self.data = element
		self.right = None
		self.left = None

class BST:
	root = None
	seen = {}
	noNodes = 0

	def __init__(self):
		self.seen = {}
		self.noNodes = 0

	def addNode(self,root,element):
		self.noNodes += 1
		if(self.root == None):
			self.root = Node(element)
		else:
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

	def preOrder(self,root):
		if(root == None):
			return
		print(root.data,end=" ")	
		self.preOrder(root.left)
		self.preOrder(root.right)
	
	def postOrder(self,root):
		if(root == None):
			return
		self.postOrder(root.left)
		self.postOrder(root.right)
		print(root.data)
	
	def getHeightOfTree(self,root):
		if(root == None):
			return 0
		else:
			left = self.getHeightOfTree(root.left)
			right = self.getHeightOfTree(root.right)
			if(left > right):
				return left + 1
			else:
				return right + 1
			# return (max(left,right) + 1)

	def returnRandomNode(self):
		self.seen = {}
		randomNode = self.getRandomNode()
		if(randomNode in self.seen):
			self.returnRandomNode()
		else:
			return randomNode

	def getRandomNode(self):
		cnt = random.randint(0,9)# generate randome number from 0 - len nodes in tree
		print("cnt",cnt)
		def bfs(root,cnt):
			if(cnt == 0):
				return root
			q = []
			q.append(root)
			while(len(q) != 0):
				currentNode = q.pop(0)
				cnt -= 1
				if(cnt == 0):
					return currentNode
				if(currentNode.left != None):
					q.append(currentNode.left)
				if(currentNode.right != None):
					q.append(currentNode.right)
		return bfs(self.root,cnt)

if __name__ == '__main__':
	obj = BST()
	nodes = [5,4,3,2,1,10,20,30,40]
	for n in nodes:
		obj.addNode(obj.root,n)
	obj.inOrder(obj.root)
	print("\nHeight of BST tree",obj.getHeightOfTree(obj.root))
	randomNode = obj.returnRandomNode()
	print("Random node which is super fair !",randomNode.data)