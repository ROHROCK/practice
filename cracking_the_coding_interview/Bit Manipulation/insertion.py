# Insertion: You are given two 32-bit numbers, Nand M, and two bit positions, i and j. Write a method
# to insert M into N such that M starts at bit j and ends at bit i. You can assume that the bits j through
# i have enough space to fit all of M. That is, if M = 18811, you can assume that there are at least 5
# bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully
# fit between bit 3 and bit 2.
# 5.1
# EXAMPLE
# Input:
# N
# Ul811 , i
# 2, j
# 6
# Output: N = 18881881188

if __name__ == '__main__':
    standard_input = "10000000000 \n 10011 \n 2 6"
    m = int(input())
    n = int(input())
    i,j = map(int,input().split())
    print(12 & 13)
