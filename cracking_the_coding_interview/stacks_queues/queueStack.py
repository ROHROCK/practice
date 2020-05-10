# Problem number 4
# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
class Stack:
	top = None
	st = None
	
	def __init__(self):
		super().__init__()
		self.st = []
		self.top = -1

	def push(self,element):
		self.st.append(element)
		self.top += 1
	
	def pop(self):
		if(self.top == -1):
			print("Stack underflow")
			return
		popped = self.st.pop()
		self.top -= 1
		return popped
	
	def peek(self):
		return self.st[top]
	
	def printStack(self):
		return self.st
	def length(self):
		return len(self.st)


class myQueue:
	newStack = Stack()
	oldStack = Stack()

	def enqueue(self,element):
		# print(self.oldStack.length())
		if(self.oldStack.length() == 0):
			# print("inserting into new stack")
			self.newStack.push(element)
		elif(self.newStack.length() == 0 and self.oldStack.length() != 0):
			# transfer oldstack to newstack
			while(self.oldStack.length() != 0):
				self.newStack.push(self.oldStack.pop())
			self.newStack.push(element)
		
	def dequeue(self):
		popped = -1
		# check if old stack is not empty
		if(self.oldStack.length() == 0 and self.newStack.length() == 0):
			print("Queue is empty")
			return
		elif(self.oldStack.length() >= 1 and self.newStack.length() == 0):
			print("Removing element from oldstack")
			popped = self.oldStack.pop()
		elif(self.oldStack.length() == 0 and self.newStack.length() >= 1):
			print("Transfering elements from new stack to old stack")
			while(self.newStack.length() > 0):
				self.oldStack.push(self.newStack.pop())
			self.printQueue()
			popped = self.oldStack.pop()
		return popped
	
	def printQueue(self):
		print("New stack",self.newStack.printStack())
		print("Old stack",self.oldStack.printStack())

if __name__ == '__main__':
	queueObj = myQueue()
	queueObj.enqueue(1)
	queueObj.enqueue(2)
	# print(queueObj.printQueue())
	print(queueObj.dequeue()) # remove 1
	queueObj.enqueue(3)
	print(queueObj.dequeue()) # remove 2
	queueObj.enqueue(4)
	# queueObj.printQueue()