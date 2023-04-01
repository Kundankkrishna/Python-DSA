#count the number of prime numbers less than a given number A

num = int(input("Enter a number: "))
import math
def countprimes(A):
    primecount =0
    for n in range(1,A):
        sqr = int(math.sqrt(n))
        factcount = 0
        for i in range(1,sqr+1):
            if n%i ==0:
                if n/i == i:
                    factcount +=1
                else:
                    factcount +=2
        if factcount ==2:
            primecount +=1
    return primecount

print(countprimes(num))     # prints the count of prime numbers less than num.