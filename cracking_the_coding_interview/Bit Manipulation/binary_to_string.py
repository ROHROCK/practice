# Binary to String: Given a real number between 8 and 1 (e.g., 0.72) that is passed in as a double,
# print the binary representation. If the number cannot be represented accurately in binary with at
# most 32 characters, print "ERROR:
if __name__ == '__main__':
    standard_input = "0.5"
    realNumber = input()
    if(len(realNumber) > 32):
        print("Error")
    realNumber = float(realNumber)
    if(realNumber < 0 or realNumber > 1):
        print("Error")
    print(realNumber)
    ans = "."
    # also a correct solution
    # while(realNumber > 0):
    #     if(len(str(realNumber)) >= 32):
    #         print("Exceeded 32 bit")
    #         break
    #     res = realNumber * 2
    #     if(res >= 1):
    #         ans += "1"
    #         realNumber -= 1
    #     else:
    #         ans += "0"
    #         realNumber = res
    frac = 0.5
    while(realNumber > 0):
        if(len(str(realNumber)) >= 32):
            print("Exceeded 32 bit")
            break
        if(realNumber >= frac):
            ans += "1"
            realNumber -= frac
        else:
            ans += "0"
        frac /= 2
    print(ans)