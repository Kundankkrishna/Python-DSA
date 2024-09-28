# Problem Description
#
# Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array
#
# and at least one occurrence of the minimum value of the array.
#
# Problem Constraints
#
# 1 <= |A| <= 2000
#
# Input Format
#
# First and only argument is vector A
#
# Output Format
#
# Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array
#
# Example Input,
#
# Input 1:
#
# A = [1, 3, 2]
# Input 2:
#
# A = [2, 6, 1, 6, 9]
#
# Example Output,
#
# Output 1:
#
#  2
# Output 2:
#
#  3
#
# Example Explanation,
#
# Explanation 1:
#
#  Take the 1st and 2nd elements as they are the minimum and maximum elements respectievly.
# Explanation 2:
#
#  Take the last 3 elements of the array.


def closestminmax(arr):
    ans = len(arr)  # initializing the ans to the length of array as this will surely contain the min and max in array.
    minm = min(arr)
    maxi = max(arr)
    if minm == maxi: # if min and max values are same then length of subarray containing them is 1
        return 1

    minidx = -1
    maxidx = -1

    for i in range(len(arr)):
        if arr[i] == minm:
            minidx = i
            if maxidx != -1:
                diff = abs(maxidx - minidx) + 1
                ans = min(diff, ans)

        if arr[i] == maxi:
            maxidx = i
            if minidx != -1:
                diff = abs(minidx - maxidx) + 1
                ans = min(diff, ans)

    return ans

print(closestminmax([1, 2, 3, 4, 5,10, 6, 7, 8,1, 9, 10]))
