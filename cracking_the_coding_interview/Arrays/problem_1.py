# Implement an algorithm to determine if a string has all unique characters . What if you cannot use additional 
# data structure 
strArray = input()
setArray = set(strArray)
print(len(setArray) == len(strArray))