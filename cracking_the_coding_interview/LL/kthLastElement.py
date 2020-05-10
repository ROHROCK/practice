import pytest

class node:
	def __init__(self,data):
		self.data = data
		self.next = None
class LL:
	def createLL(self,l):
		if(len(l) == -1):
			return -1
		head = node(l[0])
		headCopy = head
		for num in l[1:]:
			head.next = node(num)
			head = head.next
		return headCopy
	def printLL(self,node):
		while(node != None):
			print(node.data,sep=" ",end=" ")
			node = node.next
		print()

# solution which interview might not be happy with .. trival solution
def solution(head,k):
	counter = 0
	headCopy = head
	while(head != None):
		counter += 1
		head = head.next
	counter = counter - k
	while(counter != 0):
		counter-=1
		headCopy = headCopy.next
	return headCopy.data

# recursive solution , but still it is having huge space complexity O(n) since you
# have to traverse the link list

def printKthElementRecursively(node,k):
	if(node == None):
		return 0
	index = printKthElementRecursively(node.next,k) + 1
	if(index == k):
		print("The node at kth last index is: ",node.data)
	return index

# def little optimal solution , time complexity is still O(N)
# approach: Make two pointers , make both pointer have distance k between themselves and
# simply just traverse the list till the end , when p2 is at the end return p1 as it is at the
# correct place
def optimalSolution(head,k):
	pointerA = head
	pointerB = head
	for i in range(k):
		if(pointerA == None):
			return -1
		pointerA = pointerA.next
	while(pointerA != None):
		pointerA = pointerA.next
		pointerB = pointerB.next
	print(pointerB.data)

if __name__ == '__main__':
	v = LL()
	h = v.createLL([1,2,3,4,5])
	# print(solution(h,1))
	printKthElementRecursively(h,3)
	optimalSolution(h,3)