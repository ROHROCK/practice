import pytest
# to remove dups from link list
class Node:
	def __init__(self,data):
		self.next = None
		self.data = data
# using memory
def main(head):
	seen = set([])
	prev = None
	h = head
	while(head != None):
		if(head.data in seen):
			prev.next = head.next
		else:
			seen.add(head.data)
			prev = head
		head = head.next
	return h
# without using memory
def WOmain(head):
	current = head
	while(current != None):
		runner = current
		while(runner.next != None):
			if(runner.next.data == current.data):
				runner.next = runner.next.next
			else:
				runner = runner.next
		current = current.next
	return head
# to print the link list
def printLinkList(Head):
	temp = []
	while(Head != None):
		temp.append(Head.data)
		Head = Head.next
	return temp
#create link list
def createLL(numList):
	head = Node(numList[0])
	headCopy = head
	for num in numList[1:]:
		head.next = Node(num)
		head = head.next
	return headCopy

def test():
	head = createLL([10 ,12 ,11 ,11 ,12 ,11 ,10])
	main(head)
	aL = printLinkList(head)
	assert [10,12,11] == aL
	head = createLL([1,5,7,10])
	newHead = main(head)
	aL = printLinkList(newHead)
	assert [1,5,7,10] == aL

def test_1():
	head = createLL([10 ,12 ,11 ,11 ,12 ,11 ,10])
	WOmain(head)
	aL = printLinkList(head)
	#print(aL)
	assert [10,12,11] == aL
	head = createLL([1,5,7,10])
	newHead = WOmain(head)
	aL = printLinkList(newHead)
	assert [1,5,7,10] == aL

# test()
test_1()