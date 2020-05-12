# Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.
from minimalTree import createTree
import Newtree
def inOrderSuccessor(node):
	if(node == None):
		return None
	if(node.right != None):
		return leftMostChild(Node.right)
	else:
		copyNode = node
		parentNode = copyNode.parent
		while(parentNode != None and parentNode.left != copyNode):
			copyNode = parentNode
			parentNode = parentNode.parent
		return parentNode

def leftMostChild(node):
	if(node == None):
		return None
	while(node.left != None):
		node = node.left
	return node

if __name__ == '__main__':
	# obj = createTree()
	# root = obj.solution([3,1,2,5,20,10,30])
	# print(root.preOrder(root.getRoot()))
	# print(root.getHeightOfTree(root.getRoot()))
	# obj.inOrder(root)
	newobj = Newtree.NewTree()
	newobj.addNode([50,1,2,3,100,200,150,90])
	newobj.printTree()	