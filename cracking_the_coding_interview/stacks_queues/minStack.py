import sys

class stack:
	st = []
	top = -1
	minStack = []
	
	def push(self,element):
		self.top += 1
		# if the element inserted is lower than current min element in stack
		if(element <= self.minElement()):
			self.minStack.append(element)
		self.st.append(element)

	def minElement(self):
		if(len(self.minStack) == 0):
			return float('inf')
		else:
			return self.minStackPeek()
	
	def minStackPeek(self):
		return self.minStack[-1]
	
	# becomes O(n) which is not desirable
	# def pop(self):
	# 	if(self.top <= -1):
	# 		print("Stack underflow !")
	# 		return
	# 	poppedElement = self.st.pop(self.top)
	# 	self.top -= 1
	# 	if(self.top == -1):
	# 		self.minPointer = -1
	# 		return poppedElement
	# 	self.minPointer = self.st.index(min(self.st))
	# 	return poppedElement
	
	def pop(self):
		if(self.top <= -1):
			print("Stack underflow !")
			return
		popped = self.st.pop(self.top)
		self.top = self.top - 1 
		if(popped == self.minStack[-1]):
			self.minStack = self.minStack[:-1]
		return popped

	def peek(self):
		if(self.top == -1):
			print("Stack empty")
			return
		return self.st[self.top]

if __name__ == "__main__":
	obj = stack()

	obj.push(5)
	print("Min Element",obj.minStackPeek())
	obj.push(6)
	print("Min Element",obj.minStackPeek())
	obj.push(3)
	print("Min Element",obj.minStackPeek())
	obj.push(7)
	print("Min Element",obj.minStackPeek())
	
	obj.pop()
	print("Min Element",obj.minStackPeek())
	obj.pop()
	print("Min Element",obj.minStackPeek())
