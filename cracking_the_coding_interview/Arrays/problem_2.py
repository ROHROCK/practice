# Problem statement: Given two strings , write a method to decide if one is permutation of the other.

# the input string are made lower case and removed of any white spaces
str1 = input().strip().lower()
str2 = input().strip().lower()
dictionaryDict = set(str1)
if(len(str1) != len(str2)):
    print("False")
else:
    print(str1 == str2)