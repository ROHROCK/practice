import math

class node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class tree:
	total = 0
	l = []
	key = 0
	path = []
	def __init__(self):
		self.root = None
		self.path = []

	def insertInOrder(self,listOfNodes):
		listNodes = []
		listNodes.append(node(listOfNodes[0]))
		self.root = listNodes[0]
		for i in range(1,len(listOfNodes)):
			# print(listNodes)
			if(i % 2 != 0):
				rootIndex = math.floor(i // 2)
				# print(rootIndex)
				temp = node(listOfNodes[i])
				listNodes[rootIndex].left = temp
				listNodes.append(temp)
			else:
				rootIndex = math.floor(i // 2) -1
				# print(rootIndex)
				temp = node(listOfNodes[i])
				listNodes[rootIndex].right = temp
				listNodes.append(temp)
		
	
	def printLevelOrder(self,root):
		# print(root)
		q = []
		q.append(root)
		levelCnt = 0
		while(len(q) != 0):
			levelCnt = len(q)
			while(levelCnt != 0):
				currentNode = q.pop(0)
				print(currentNode.data,end=' ')
				# self.pathFromRoot(currentNode,[])
				if currentNode.left != None:
					q.append(currentNode.left)
				if(currentNode.right != None):
					q.append(currentNode.right)
				levelCnt -= 1
			print()
		print('Answer: ',self.path)
	
	def pathFromNode(self,root):
		if(root == None):
			return 0
		pathsFromRoot = self.countPathsWithSumFromNode(root,0)
		left = self.pathFromNode(root.left)
		right = self.pathFromNode(root.right)

		return pathsFromRoot + left + right
	
	# implements sliding window algorithm to find the path
	def countPathsWithSumFromNode(self,node,currentSum):
		if(node == None):
			return 0
		
		currentSum += node.data
		totalPath = 0
		if(currentSum == self.key):
			totalPath += 1

		totalPath += self.countPathsWithSumFromNode(node.left,currentSum)
		totalPath += self.countPathsWithSumFromNode(node.right,currentSum)

		return totalPath

	def printPath(self):
		print(self.path)



if __name__ == '__main__':
	treeRootObject = tree()
	nodes = [5,3,1,-2,0,-1,5]
	treeRootObject.insertInOrder(nodes)
	treeRootObject.key = 6
	# treeRootObject.printLevelOrder(treeRootObject.root)
	# treeRootObject.pathFromRoot(treeRootObject.root,[])
	print(treeRootObject.pathFromNode(treeRootObject.root))