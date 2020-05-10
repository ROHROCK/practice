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

def solution(head):
	headCpy = head
	length = 0
	while(headCpy != None):
		length += 1
		headCpy = headCpy.next
	midPtr = None
	headCpy = head
	goal = length // 2

	while(length != goal):
		length -=1
		prev = headCpy
		headCpy = headCpy.next
	prev.next = None	
	midPtr = headCpy
	o = LL()
	# reverse the second half of the LL
	# o.printLL(midPtr)
	# o.printLL(head)

	prev = midPtr
	midPtr = midPtr.next
	prev.next = None
	while(midPtr != None):
		nextNode = midPtr.next
		midPtr.next = prev
		prev = midPtr
		midPtr = nextNode
	# o.printLL(prev)

	midPtr = prev
	# check if palindrome
	while(midPtr != None):
		if head.data != midPtr.data:
			print("Not a Palindrome")
			return
		midPtr= midPtr.next
		head = head.next
	print("Palindrome LL")
	return 

if __name__ == '__main__':
	obj = LL()
	head = obj.createLL([1,2,3,3,1,2])
	solution(head)