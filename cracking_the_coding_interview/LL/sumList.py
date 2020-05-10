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

def solution1(head1,head2):
	sumHead = None
	carry = 0
	cpy = None
	while(head1 != None):
		if(carry):
			number = 1
		else:
			number = 0
		number += head1.data + head2.data
		if(number > 10):
			number = number%10
			carry = 1
		else:
			carry = 0
		node = Node(number)
		print(number)
		if(sumHead == None):
			sumHead = node
			cpy = sumHead
		else:
			sumHead.next = node
			sumHead = sumHead.next
		head1 = head1.next
		head2 = head2.next
	if(carry == 1):
		sumHead.next = Node(1)
	return cpy

# when the places are in reverse order
def solution2(head1,head2):
	sumHead = None
	carry = 0
	cpy = None
	carryHead = None
	cpyCarryHead = carryHead
	while(head1 != None):
		number = head1.data + head2.data
		if(number >= 10):
			number = number%10
			carry = 1
		else:
			carry = 0
		node = Node(carry)

		if(carryHead == None):
			carryHead = node
			cpyCarryHead = carryHead
		else:
			carryHead.next = node
			carryHead = carryHead.next
		
		node = Node(number)
		# print(number)
		if(sumHead == None):
			sumHead = node
			cpy = sumHead
		else:
			sumHead.next = node
			sumHead = sumHead.next
		head1 = head1.next
		head2 = head2.next
	
	cpyCarryHead = cpyCarryHead.next
	cpyRet = cpy
	while(cpyCarryHead != None):
		cpy.data += cpyCarryHead.data
		cpyCarryHead = cpyCarryHead.next
		cpy = cpy.next
	return cpyRet

if __name__ == '__main__':
	obj = LL()
	head1 = obj.createLL([6,1,7])
	head2 = obj.createLL([2,9,5])
	obj.printLL(solution2(head1,head2))