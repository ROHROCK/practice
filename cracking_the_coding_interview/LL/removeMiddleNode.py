class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
class LL:
	def createLL(self,nodelist):
		head = Node(nodelist[0])
		headCopy = head
		for num in nodelist[1:]:
			head.next = Node(num)
			head = head.next
		return headCopy
	def printLL(self,head):
		while(head != None):
			print(head.data,sep=" ",end=" ")
			head = head.next

# goal : to delete node from middle
# approach: use two pointers , prev and current , when current.data == goal , just replace it 
# by doing prev.next = current.next , this works only on middle nodes only
# works only when you have the head of the link list
# head is Node class , nodeToRemove is number which you want to remove
def solution1(head,nodeToRemove):
	current = head
	prev = None
	while(current != None):
		if(nodeToRemove == current.data):
			prev.next = current.next
		prev = current
		current = current.next
	return head
	
# Here there is no head of the LL given , only the actual node by reference is given which
# is expected to be deleted.
# Approach: simply copy the content to next node , and delete the next node
def solution2(nodeToRemove):
	nextNode = nodeToRemove.next
	nodeToRemove.data = nextNode.data
	nodeToRemove.next = nextNode.next
	del nextNode

if __name__ == '__main__':
	obj = LL()
	head = obj.createLL([1,2,3,4,5,6])
	beforeHead = head
	obj.printLL(beforeHead)
	# newHead = solution1(head,2)
	solution2(head.next)
	print()
	obj.printLL(head)