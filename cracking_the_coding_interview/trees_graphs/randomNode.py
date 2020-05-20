import random

class Node:
	def __init__(self,element):
		self.data = element
		self.right = None
		self.left = None
		self.size = 1
	
	def getIthNode(self,ithIndex):
		leftSize = 0 if self.left == None else self.left.size
		if(ithIndex < leftSize):
			return self.left.getIthNode(ithIndex)
		elif(ithIndex == leftSize):
			return self
		else:
			return self.right.getIthNode(ithIndex - (leftSize+1))
		
	def insertInOrder(self,d):
		if(d <= self.data):
			if(self.left == None):
				self.left = Node(d)
			else:
				self.left.insertInOrder(d)
		else:
			if(self.right == None):
				self.right = Node(d)
			else:
				self.right.insertInOrder(d)
		self.size += 1
	
	def size(self):
		return self.size

class Tree:
	root = None

	def __init__(self):
		self.noNodes = 0
	
	def size(self):
		return 0 if self.root == None else root.size

	def getRandomNode(self):
		if(self.root == None):
			return None
		randIndex = random.randint(0,self.root.size-1)
		# print('randIndex',randIndex)
		return self.root.getIthNode(randIndex)

	def insertInOrder(self,value):
		if(self.root == None):
			self.root = Node(value)
		else:
			self.root.insertInOrder(value)

if __name__ == '__main__':
	obj = Tree()
	nodes = [5,4,3,2,1,10,20,30,40]
	for n in nodes:
		obj.insertInOrder(n)
	random = obj.getRandomNode()
	print(random.data)