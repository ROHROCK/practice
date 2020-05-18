from tree import BST
from itertools import permutations

def allSequence(node):
	result = []
	if(node == None):
		result.append(LL())
		return result
	prefix = []
	prefix.add(node.data)

	leftSequence = allSequence(node.left)
	rightSequence = allSequence(node.right)

	while(leftSequence.getHead() != None):
		while(rightSequence.getHead() != None):
			weaved = []
			weaveLists(leftSequence,rightSequence,weaved,prefix)
			result.append(weaved)
			rightSequence = rightSequence.getNext()
		leftSequence = leftSequence.getNext()

def weaveLists(left,right,results,prefix):
	if(len(left) == 0):
		result = prefix.copy()
		result.append(left)
		results.append(result)
		return
	else:
		result = prefix.copy()
		result.append(right)
		results.append(result)
		return
	
	headFirst = left.removeFirst()
	weaveLists(left,right,results,prefix)
	prefix.removeLast()
	left.addFirst(headFirst)

	headsecond = right.removeFirst()
	weaveLists(right,right,results,prefix)
	prefix.removeLast()
	right.addFirst(headsecond)
	
if __name__ == '__main__':
	treeObj = BST()
	numberList = [50,30,100,20,35,200,40,150]
	for number in numberList:
		treeObj.addNode(treeObj.root,number)