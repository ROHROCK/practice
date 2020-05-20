import math

class node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class tree:
	total = 0
	l = []
	def __init__(self):
		self.root = None

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
				if currentNode.left != None:
					q.append(currentNode.left)
				if(currentNode.right != None):
					q.append(currentNode.right)
				levelCnt -= 1
			print()
	
	def pathFromRoot(self,root,l):
		if(root == None):
			return None
		l.append(root.data)
		self.checkPath(l)
		left = self.pathFromRoot(root.left,l)
		right = self.pathFromRoot(root.right,l)
		del l[-1]
	
	def checkPath(self,l):
		cnt = 0
		print(l)
		return cnt


if __name__ == '__main__':
	treeRootObject = tree()
	nodes = [5,3,1,-2,0,-1,10]
	treeRootObject.insertInOrder(nodes)
	treeRootObject.printLevelOrder(treeRootObject.root)
	treeRootObject.pathFromRoot(treeRootObject.root,[])