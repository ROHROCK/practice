from tree import BST
# from collections import deque

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
		customRoot.left = customNode(root.left.data,root)
	if(root.right != None):
		customRoot.right = customNode(root.right.data,root)

	copyTree(root.left,customRoot.left)
	copyTree(root.right,customRoot.right)

	return customRoot

# my approach to create a new tree with parent data
def solution(root):
	newRoot = customNode(root.data,None)
	newTreeRoot = copyTree(root,newRoot)
	return newRoot

if __name__ == '__main__':
	treeObj = BST()
	numberList = [4,2,3,7,5,6]
	for number in numberList:
		treeObj.addNode(treeObj.root,number)
	# treeObj.inOrder(treeObj.root)
	newTreeRoot = solution(treeObj.root)
	print('Special Tree')
	treeObj.inOrder(newTreeRoot)