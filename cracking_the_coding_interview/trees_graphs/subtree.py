from tree import BST

#  total time complexity is O(n + m) where n is the total node in T1 
# and m is the total nodes in T2
def checkSubTree(root1,root2):
	if(root1 == None):
		return None
	if(root2 == None):
		return None
	# check if the number of nodes are equal or not
	if((root1.right == None and root2.right != None) or 
	(root1.right != None and root2.right == None)):
		return None
	if((root1.left == None and root2.left != None) or 
	(root1.left != None and root2.left == None)):
		return None

	# print(root1.data,root2.data)
	# the check the data value
	if(root1.data != root2.data):
		return None
	resLeft = checkSubTree(root1.left,root2.left)
	resRight = checkSubTree(root1.right,root2.right)
	if(resLeft == None or resRight == None):
		return False

	return True
def keyNodeInT1(root,key):
	if root == None:
		return None

	left = keyNodeInT1(root.left,key)
	right = keyNodeInT1(root.right,key)

	if(left != None):
		if(left.data == key):
			return left

	if(right != None):
		if(right.data == key):
			return right

	return root

if __name__ == '__main__':
	createtree = BST()
	nodes = [10,5,30,4,25,35,1,20,23,32,40,0,2]
	node1 = [1,0,2]
	createSubtree = BST()
	for n in node1:
		createSubtree.addNode(createSubtree.root,n)
	for n in nodes:
		createtree.addNode(createtree.root,n)
	# createtree.inOrder(createtree.root)
	keyNode = keyNodeInT1(createtree.root,1) # return closest node
	print("keynode found: ",keyNode.data)
	print(checkSubTree(keyNode,createSubtree.root))