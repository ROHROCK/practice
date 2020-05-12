# Minimal Tree: Given a sorted (increasing order) array with unique integer 
# elements, write an algorithm to create a binary search tree with minimal height.
from tree import BST

# input : [] output: None
class createTree:
	def solution(self,answerList):
		if(answerList == None):
			return
		else:
			middle = answerList[len(answerList)//2]
			left = answerList[:len(answerList)//2]
			right = answerList[(len(answerList)//2)+1:]
			obj = BST()
			obj.addNode(obj.root,middle)
			for l in left:
				obj.addNode(obj.root,l)
			for r in right:
				obj.addNode(obj.root,r)
			# obj.inOrder(obj.root)
			# print("Height of tree:",obj.getHeightOfTree(obj.root))
			return obj
	def inOrder(self,obj):
		obj.inOrder(obj.root)

# if __name__ == '__main__':
	# solution([1,2,3,4,5,6])