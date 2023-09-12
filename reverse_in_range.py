# Given an array A of N integers and also given two integers B and C. 
# Reverse the elements of the array A within the given inclusive range [B, C].

num = int(input("Enter the length of the array: "))
A = []

for i in range(0, num):
  element = int(input("enter the element: "))
  A.append(element)


B = int(input("Enter the value of B: "))
C = int(input("Enter the value of C: "))


def reverseInRange(A, B, C):
  while B < C:
      temp = A[B]
      A[B] = A[C]
      A[C] = temp
      B += 1
      C -= 1
  
  return A


print(reverseInRange(A, B, C))
