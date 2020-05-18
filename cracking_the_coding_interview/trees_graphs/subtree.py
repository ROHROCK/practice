from tree import BST

#  total time complexity is O(n + m) where n is the total node in T1 
# and m is the total nodes in T2
def checkSubTree(root1,root2):
	if(root1 == None and root2 == None):
		return True
	elif(root1 == None or root2 == None):
		return False
	elif(root1.data != root2.data):
		return False
	else:
		return checkSubTree(root1.left,root2.left) and checkSubTree(root1.right,root2.right)

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