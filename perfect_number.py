# You are given an integer A. You have to tell whether it is a perfect number or not.

import math
def solve(A):
        summ = 0
        sqr = int(math.sqrt(A))
        for i in range(1,sqr+1):
            if A%i == 0:
                if A/i ==i:
                    summ +=i
                else:
                    summ = summ + i +A/i
        if summ == 2*A:
            return 1
        else:
            return 0