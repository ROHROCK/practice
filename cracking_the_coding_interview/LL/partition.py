class Node:
	def __init__(self,data):
	 self.data = data
	 self.next = None

class LL:
	def createLL(self,listNode):
		if(len(listNode) == 0):
			print("Can't create LL for empty list")
			return None
		head = Node(listNode[0])
		headCopy = head
		for num in listNode[1:]:
			head.next = Node(num)
			head = head.next
		return headCopy
	def printLL(self,node):
		while(node != None):
			print(node.data,sep=" ",end=" ")
			node = node.next

# smart solution !
def solution(node,val):
	head,tail = node,node
	while(node != None):
		# print(1)
		nextNode = node.next
		if(node.data < val):
			node.next = head
			head = node
		else:
			tail.next = node
			tail = node
		node = nextNode
	tail.next = None

	return head

if __name__ == '__main__':
	obj = LL()
	head = obj.createLL([3,5,8,5,10,2,1])
	# for testing
	# obj.printLL(head)
	obj.printLL(solution(head,5))
	