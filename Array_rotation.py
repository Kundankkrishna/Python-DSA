# Rotating an array from last to first k times.
arr = []
num = int(input("Enter the number of elements in the array: "))
for ind in range(0, num):
    arr.append(int(input()))
print(arr)
k = int(input("Enter the number of rotations: "))
if k > num:
    k = k % num


def segmentreverse(arr, start, end):
    p1 = start
    p2 = end
    while p1 < p2:
        temp = arr[p1]
        arr[p1] = arr[p2]
        arr[p2] = temp
        p1 += 1
        p2 -= 1
    return arr


# print(segmentreverse(arr,start,end))
# step 1 , reverse the whole array. for this we need to set the start and end indices as the first and last index of the
# array respectively.

reversedarray = segmentreverse(arr, 0, num - 1)
# print("Whole array reversed : ",reversedarray)
# step 2, reverse the first k elements of the reversed array.

firstpartreversed = segmentreverse(reversedarray, 0, k-1)
# print("First k elements reversed: ",firstpartreversed)

# step 3, reverse the rest of the elements in the array after the first k elements.

finalarray = segmentreverse(firstpartreversed, k, num - 1)

print("Final array after rotation: ", finalarray)
