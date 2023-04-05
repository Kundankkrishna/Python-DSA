# Check if a number is prime or not

import math
num = int(input("Enter number: "))
def primeChecker(x):
    count = 0
    undrt = int(math.sqrt(x))
    for i in range(2,undrt+1):
        if x%i == 0:
            count = count + 1
    if count > 0:
        print("not prime")
    else:
        print("prime")
primeChecker(num)