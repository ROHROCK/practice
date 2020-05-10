import time,datetime
class node:
	timestamp = None
	pet = None

	def __init__(self,petType):
		self.timestamp = time.mktime(datetime.datetime.today().timetuple())
		self.pet = petType

class animalShelter:
	dogQueue = None
	catQueue = None

	def __init__(self):
		self.dogQueue = []
		self.catQueue = []
	
	def peekDog(self):
		if(len(self.dogQueue) == None):
			print("Dog queue is empty")
			return None
		temp = self.dogQueue[-1]
		return temp

	def peekCat(self):
		if(len(self.catQueue) == None):
			print("Cat queue is empty")
			return None
		temp = self.catQueue[-1]
		return temp

	def dequeue(self):
		dogPeek = self.peekDog()
		catPeek = self.peekCat()
		if(dogPeek == None and catPeek == None):
			print("Animal shelter is empty")
			return None
		elif(dogPeek == None):
			return self.catQueue.pop()
		elif(catPeek == None):
			return self.dogQueue.pop()
		if(dogPeek.timestamp > catPeek.timestamp):
			return self.dogQueue.pop()
		else:
			return self.catQueue.pop()
	def dequeueDog(self):
		if(len(self.dogQueue) == 0):
			print("Sorry no dogs are available")
			return None
		return self.dogQueue.pop()

	def dequeueCat(self):
		if(len(self.dogQueue) == 0):
			print("Sorry no catss are available")
			return None
		return self.catQueue.pop()
	
	def enqueue(self,element):
		temp = node(element)
		if(element == "cat"):
			self.catQueue.insert(0,temp)
			print(self.catQueue)
		elif(element == "dog"):
			self.dogQueue.insert(0,temp)
			print(self.dogQueue)

if __name__ == '__main__':
	obj = animalShelter()
	obj.enqueue("cat")
	obj.enqueue("cat")
	obj.enqueue("cat")
	obj.enqueue("dog")

	temp = obj.dequeue()
	print(temp.pet)

	temp = obj.dequeueDog()
	print(temp.pet)