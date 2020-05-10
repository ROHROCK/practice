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
		return 

	def pop(self):
		if(self.top == -1):
			print("Stack underflow")
			return
		popped = self.st.pop()
		self.top -= 1
		return popped
	
	def peek(self):
		if(len(self.st) == 0):
			return None
		return self.st[-1]
	
	def printStack(self):
		return self.st

	def length(self):
		return len(self.st)

class sortStack:
	mainStack = Stack()
	tempStack = Stack()

	def pushElement(self,element):
		if(self.mainStack.length() == 0):
			self.mainStack.push(element)
		elif(self.mainStack.peek() > element):
			self.mainStack.push(element)
		else:
			while(element > self.mainStack.peek()):
				self.tempStack.push(self.mainStack.pop())
				if(self.mainStack.peek() == None):
					break
			self.mainStack.push(element)
			# reverse the operation
			while(self.tempStack.length() != 0):
				self.mainStack.push(self.tempStack.pop())
	
	def minElement(self):
		return self.mainStack.peek()
	
	def printStack(self):
		print(self.mainStack.printStack())
		return
	
if __name__ == '__main__':
	obj = sortStack()
	# test case 1
	# obj.pushElement(3)
	# obj.pushElement(2)
	# obj.pushElement(1)
	# obj.printStack() # should have [3,2,1]
	# test case 2
	obj.pushElement(10)
	obj.pushElement(1)
	obj.pushElement(5)
	obj.printStack() # should have [10,5,1]