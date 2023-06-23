# count the number of elements having at least 1 element greater than itself

num = int(input("Enter the size of array: "))
A = []
for i in range(0, num):
    elements = int(input("Enter element: "))
    A.append(elements)


def countGreater(array):
    maxim = array[0]
    frequency = 0
    for i in range(0, len(array)):
        if array[i] == maxim:
            frequency += 1
        if array[i] > maxim:
            maxim = array[i]
            frequency = 1
    return len(array) - frequency


print(countGreater(A))
