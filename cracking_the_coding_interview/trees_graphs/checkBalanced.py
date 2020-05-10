# Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.
from tree import BST

# set -2 as the error code
def getHeight(root):
	if(root == None):
		return -1

	left = getHeight(root.left)
	
	if(left == float('-inf')):
		return float('-inf')

	right = getHeight(root.right)
	if(right == float('-inf')):
		return float('-inf')
	
	if(abs(left - right) > 1):
		return float('-inf')
	else:
		return max(left,right)+1

def checkBalanced(root):
	print(getHeight(root))
	return getHeight(root) != float('-inf')

if __name__ == '__main__':
	createTree = BST()

	elements = [4,6,5,3,2,9,1]
	for e in elements:
		createTree.addNode(createTree.root,e)
	# tree = createTree.solution([1,2,3,4,6,5])
	print(checkBalanced(createTree.root))