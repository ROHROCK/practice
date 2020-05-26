primeOrNot = [0]*10005
def prime_sieve():
    for i in range(3,10005,2):
        primeOrNot[i] = 1
    for j in range(3,10005,2):
        if(primeOrNot[j] == 1):
            # print(j)
            # mark all the multiples of j as not prime
            for z in range(j*j,10005,j):
                primeOrNot[z] = 0
    primeOrNot[2] = 1

standard_input="2 \n 1 10\n 11 20"
t = int(input())
prime_sieve()
for _ in range(t):
    start,end = map(int,input().split())
    ans = 0
    for number in range(start,end+1):
        ans += primeOrNot[number]
    print(ans)
    
