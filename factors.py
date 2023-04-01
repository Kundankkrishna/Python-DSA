# count and return the factors of a number.

import math,time
num = int(input("Enter a number: "))
factors = []
start_time = time.time()

# # optimised solution 

def countFactors(x):
    count = 0
    root = int(math.sqrt(x))
    for i in range(1,root+1):
        if x%i == 0:
            if x/i ==i:
                factors.append(i)
                count = count+1
            else:
                factors.append(i)
                factors.append(int(x/i))
                count = count+2
    return count,factors

print(countFactors(num))


#  # count the factors of a number (only counting)


# import math
# num = int(input("enter number: "))
# def countFactors(x):
#     count =0
#     i =1
#     while i <= math.sqrt(x):
#         if x%i ==0:
#             if x/i == i:
#                 count = count+1
#             else:
#                 count = count+2
#         i = i+1
#     return count

# print(countFactors(num))

# # brute force for factor counting

# def factors(num):
#     count = 0
#     for i in range(1,num+1):
#         if num % i ==0:
#             count += 1
#     return count

# print(factors(num))

end_time = time.time()
exec_time = end_time - start_time
print("Execution time = ",exec_time)