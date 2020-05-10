class Node:
	def __init__(self,element):
		self.data = element
		self.right = None
		self.left = None

class BST:
	root = None

	def addNode(self,element):
		if(self.root == None):
			self.root = Node(element)
		else:
			temp = self.root
			while(temp.right != None and temp.left != None):
				if(temp.data >= element):
					temp = temp.left
				else:
					temp = temp.right
			if(temp.data < element):
				temp.right = Node(element)
			else:
				temp.left = Node(element)
	
	def inOrder(self,root):
		if(root == None):
			return
		self.inOrder(root.left)
		print(root.data,end=" ")
		self.inOrder(root.right)		

	def preOrder(self,root):
		if(root == None):
			return
		print(root.data)	
		self.preOrder(root.left)
		self.preOrder(root.right)
	
	def postOrder(self,root):
		if(root == None):
			return
		self.postOrder(root.left)
		self.postOrder(root.right)
		print(root.data)
	
	def heightOfTree(self,root):
		if(root == None):
			return 0
		else:
			left = self.heightOfTree(root.left)
			right = self.heightOfTree(root.right)
			if(left > right):
				return left + 1
			else:
				return right + 1
			# return (max(left,right) + 1)

if __name__ == '__main__':
	obj = BST()
	obj.addNode(3)
	obj.addNode(2)
	obj.addNode(1)
	obj.addNode(4)
	obj.addNode(5)
	obj.inOrder(obj.root)
	print("\nHeight of BST tree",obj.heightOfTree(obj.root))
	