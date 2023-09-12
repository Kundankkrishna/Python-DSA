# Given an array A and an integer B. A pair(i, j) in the array is a good pair
# if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.

num = int(input("Enter the size of array: "))
A = []
for i in range(0, num):
    elements = int(input("Enter element: "))
    A.append(elements)


def goodPair(A, B):
  for i in range(0, len(A) - 1):
    for j in range(i + 1, len(A)):
        if A[i] + A[j] == B:
            return 1
  return 0


print(goodPair(A))
