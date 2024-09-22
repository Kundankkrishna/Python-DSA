# Given an array of integers A, find and return the product array of the same size where the ith element of the product
# array will be equal to the product of all the elements divided by the ith element of the array.
#
# Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the
# division operator.
#
#
# Input Format
#
# The only argument given is the integer array A.
# Output Format
#
# Return the product array.
# Constraints
#
# 2 <= length of the array <= 1000
# 1 <= A[i] <= 10
# For Example
#
# Input 1:
#     A = [1, 2, 3, 4, 5]
# Output 1:
#     [120, 60, 40, 30, 24]
#
# Input 2:
#     A = [5, 1, 10, 1]
# Output 2:
#     [10, 50, 5, 50]
# Expected Output
# Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem
# understanding and test edge cases

inparr = [1, 2, 3, 4, 5, 6]


def prodarrpuzzle(array):
    prodarray = []

    def createprefixarr(arr):
        prefarr = []
        for i in range(0, len(arr)):
            # print("i is : ", i)
            if i == 0:
                prefarr.append(arr[i])
            else:
                elem = prefarr[i-1] * arr[i]
                prefarr.append(elem)

        print("prefix product array: ", prefarr)
        return prefarr

    def createsuffixarr(arr):
        suffarr = [1 for _ in range(len(arr))]
        for j in range(len(arr) - 1, -1, -1):
            # print("j is : ", j)
            if j == len(arr) - 1:
                suffarr[j] = arr[j]
            else:
                suffarr[j] = suffarr[j + 1] * arr[j]

        print("suffix product array: ", suffarr)
        return suffarr

    prefixarr = createprefixarr(array)
    suffixarr = createsuffixarr(array)

    for x in range(0, len(array)):

        if x == 0:
            prodarray.append(suffixarr[x + 1])
        elif x == len(array) - 1:
            prodarray.append(prefixarr[x - 1])
        else:
            eleme = prefixarr[x - 1] * suffixarr[x + 1]
            prodarray.append(eleme)

    return prodarray


print(prodarrpuzzle(inparr))
