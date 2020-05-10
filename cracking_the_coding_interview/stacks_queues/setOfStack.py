# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push () and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop ( ) should return the same values as it would if there were just a single stack).
class setOfStack:
	capacity = 0
	stack = [[]]
	currentStackPtr = 0
	top = -1
	
	def __init__(self,capacityPerStack):
		self.capacity = capacityPerStack - 1
	
	def push(self,element):
		if(self.top >= self.capacity):
			self.currentStackPtr += 1
			self.stack.append([element])
			self.top = 0
		else:
			self.stack[self.currentStackPtr].append(element)
			self.top += 1
		return
	def pop(self):
		if self.currentStackPtr == 0 and self.top == -1:
			print("Stack underflow !")
			return
		# if element exist in stack
		print(self.top)
		if self.top >= 0 and self.currentStackPtr >= 0:
			# when currentStack is having last element in stack and stackptr is pointing at last stack
			if self.currentStackPtr == 0 and self.top == 0:
				print("Before deleting",self.stack)
				self.stack = [[]]
				print("After deleting",self.stack)
				self.currentStackPtr = 0
				self.top = -1	
			elif self.currentStackPtr > 0 and self.top == 0:
				#when there are min 2 stacks available and top is pointing at last element of current stack
				print("Before deleting",self.stack)
				del self.stack[self.currentStackPtr]
				print("After deleting",self.stack)
				self.currentStackPtr -= 1
				self.top = self.capacity
			elif(self.top > 0):
				# simply remove single element from currentstack
				print("Before deleting",self.stack)
				self.stack[self.currentStackPtr] = self.stack[self.currentStackPtr][:-1]
				print("After deleting",self.stack)
				self.top -= 1
	def popAt(self,index):
		return self.leftShift(index,True)

	def leftShift(self,index,removeTop):
		removedItem = -1	
		if(removeTop):
			removedItem = self.stack[index].pop()
		else:
			removedItem = self.removeBottom(index)
		if(len(self.stack[index]) == 0):
			del stack[index]
		elif(len(self.stack) > index+1):
			elementToInsert = self.leftShift(index+1,False)
			self.stack[index].append(elementToInsert)
		
		return removedItem
	def removeBottom(self,index):
		print("Remove bottom from",index)
		return self.stack[index].pop(0)
if __name__ == "__main__":
	obj = setOfStack(3)
	obj.push(2)
	obj.push(3)
	obj.push(4)
	obj.push(5)
	obj.push(7)
	print(obj.stack)
	print(obj.popAt(0))
	print(obj.stack)
	# obj.pop()
	# obj.pop()
	# obj.pop()
	# obj.pop()
	# obj.pop()