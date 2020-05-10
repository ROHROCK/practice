class Fixedstacks:
	numberOfStack = 0
	top = []
	start = []
	st = [0] * 15
	stackSize = 0
	def __init__(self,noOfs):
		self.numberOfStack = noOfs
		self.stackSize = len(self.st)//noOfs
		for i in range(0,15,self.stackSize):
			self.start.append(i)
		self.top = [-1] * (len(self.st) // self.stackSize)

	def printCompleteArray(self):
		print(self.st)

	def printStack(self,stackNumber):
		if(self.top[stackNumber] < self.start[stackNumber]):
			print('Stack %r is empty'%(stackNumber))
			return
		# print('stack %r = %r'%(stackNumber,self.st[self.start[stackNumber]:self.top[stackNumber]+1]))
		print('Compete stack %r = %r'%(stackNumber,self.st[self.start[stackNumber]:self.start[stackNumber]+self.stackSize]))

	def push(self,element,stackNumber):
		if(self.top[stackNumber] >= (self.start[stackNumber] + self.stackSize)-1):
			print("Stack %r is full "%(stackNumber))
			return
		if(self.top[stackNumber] == -1):
			self.top[stackNumber] = self.start[stackNumber]
		else:
			self.top[stackNumber] += 1
		positionToInsert = self.top[stackNumber]
		self.st[positionToInsert] = element
		print("inserted %r into stack %r successfully"%(element,stackNumber))
		#print('top %r'%(self.top[stackNumber]))
		#print('start %r'%((self.start[stackNumber] + self.stackSize)))
	def pop(self,stackNumber):
		if(self.top[stackNumber] < (self.start[stackNumber])):
			print('Stack underflow')
			return
		popped = self.st[self.top[stackNumber]]
		self.st[self.top[stackNumber]] = -1
		self.top[stackNumber] -= 1
		print('Removed %r from stack %r'%(popped,stackNumber))
if __name__ == '__main__':
	obj = Fixedstacks(3)
	obj.pop(0)
	obj.push(999,1)
	obj.printStack(1)
	obj.push(1030,0)
	obj.pop(1)
	obj.printCompleteArray()
	obj.printStack(1)
	obj.push(1030,0)
	obj.push(1030,0)
	print(len(obj.st))
	obj.printCompleteArray()
	