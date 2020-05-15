class Node:
	def __init__(self,element):
		self.data = element
		self.right = None
		self.left = None

class BST:
	root = None

	def addNode(self,root,element):
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

if __name__ == '__main__':
	obj = BST()
	obj.inOrder(obj.root)
	print("\nHeight of BST tree",obj.heightOfTree(obj.root))
	