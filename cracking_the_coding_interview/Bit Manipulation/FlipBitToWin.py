# Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
# find the length of the longest sequence of 1 s you could create.
# EXAMPLE
# Input: 1775
# Output: 8
# (or: 11011101111)
standard_input = "11011101111"
binary = int(input(),2)
print("Entered {:b}".format(binary))
currentLength = 0
prevLength = 0
maxLength = 0
while(binary != 0):
    print("{:b}".format(binary))
    if((binary & 1) == 1):
        currentLength += 1
    elif((binary & 1) == 0):
        prevLength = 0 if binary & 2 == 0 else currentLength # check if next bit is 0 
        currentLength = 0
        maxLength = max(prevLength+currentLength+1,maxLength)
    binary = binary >> 1
print(maxLength)