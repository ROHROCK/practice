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
    n = input()
    m = int(input(),2)
    i,j = map(int,input().split())
    # to print data in binary format
    # step 1 -> clear the bits in position j to i so create a mask
    mask = int("1" * len(n),2) # create all 1's
    leftside = (mask << j+1) & 0xffffffff # this helps to mask 32 bit data
    rightside = ((1 << i) - 1)
    n = int(n,2)

    print('N --> {:b}'.format(n,'b'))
    print('M --> {:b}'.format(m,'b'))

    mask = leftside | rightside
    print('Mask -> {:b}'.format(mask,'b'))

    n_cleared = n & mask
    print('{:b}'.format(n_cleared,'b'))

    # moving m in to correct position
    m = m << i

    # oring both m and n to get the answer
    print("Answer -> {:b}".format(m|n,'b'))
