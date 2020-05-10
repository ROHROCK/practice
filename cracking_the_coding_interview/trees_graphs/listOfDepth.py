# Given a binary tree, design an algorithm which creates a linked list of all
# the nodes at each depth (e.g., if you have a tree with depth D, 
# you'll have D linked lists).
from minimalTree import createTree
from llist import sllist

class Listsolution:
	answerList = []
	def __init__(self,height):
		self.answerList = [None] * height
	def sol(self,node,level):
		if(node == None):
			return 0
		else:
			if(self.answerList[level] == None):
				self.answerList[level] = sllist()
			
			self.answerList[level].append(node.data)
			
			self.sol(node.left,level+1)
			self.sol(node.right,level+1)

# from tree import BST
if __name__ == '__main__':
	obj = createTree()
	rootNode = obj.solution([1,2,3,4,5,6,7,8])
	# print("Height of tree ",rootNode.getHeightOfTree(rootNode.root))
	solutionObj = Listsolution(rootNode.getHeightOfTree(rootNode.root))
	solutionObj.sol(rootNode.root,0)
	print(solutionObj.answerList)

	