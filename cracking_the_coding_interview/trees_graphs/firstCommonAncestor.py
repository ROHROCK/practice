from tree import BST
from collections import deque

class customNode:
	parentNode = None
	data = None
	left = None
	right = None
	def __init__(self,d,parent):
	 self.parentNode = parent
	 self.data = d

def copyTree(root,customRoot):
	if(root == None):
		return None
	if(root.left != None):
		customRoot.left = customNode(root.left.data,customRoot)
	if(root.right != None):
		customRoot.right = customNode(root.right.data,customRoot)

	copyTree(root.left,customRoot.left)
	copyTree(root.right,customRoot.right)

	return customRoot

# my approach to create a new tree with parent data
def solution(root):
	newRoot = customNode(root.data,None)
	newTreeRoot = copyTree(root,newRoot)
	return newRoot

def findNode(root,key):
	if(root == None):
		print('Tree is empty')
		return
	queue = deque([])
	queue.append(root)
	while(len(queue) != 0):
		currentNode = queue.popleft()
		if(currentNode.data == key):
			return currentNode
		if(currentNode.left != None):
			queue.append(currentNode.left)
		if(currentNode.right != None):
			queue.append(currentNode.right)
	print("Key node not found !")
	# exit()
	return None

def firstAncestor(target1 , target2):
	routeTarget1 = []
	target1 = target1.parentNode
	while(target1 != None):
		routeTarget1.append(target1)
		target1 = target1.parentNode
	while(target2 != None):
		if(target2 in routeTarget1):
			return target2
		target2 = target2.parentNode
	return None

# considering both nodes contain in the tree 
def recursiveOptimalSolution(root,target1,target2):
	if(root == None):
		return root
	if(root.data == target1 or root.data == target2):
		return root
	leftPath = recursiveOptimalSolution(root.left,target1,target2)
	rightPath = recursiveOptimalSolution(root.right,target1,target2)

	if(leftPath == None):
		return rightPath
	if(rightPath == None):
		return leftPath
	return root

if __name__ == '__main__':
	treeObj = BST()
	numberList = [10,5,20,19,25]
	for number in numberList:
		treeObj.addNode(treeObj.root,number)
	newTreeRoot = solution(treeObj.root)
	print('Special Tree')
	treeObj.inOrder(newTreeRoot)
	target1 = findNode(newTreeRoot,19)
	target2 = findNode(newTreeRoot,25)
	if(target1 == None):
		print("key 1 is not found")
		exit()
	if(target2 == None):
		print("Key 2 is not found")
		exit()
	ancestor = firstAncestor(target1,target2)
	# print("Ancestor: ",ancestor.data)
	answer = recursiveOptimalSolution(treeObj.root,1,25)
	print("Ancestor: ",answer.data)
