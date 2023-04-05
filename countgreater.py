# count the number of elements having at least 1 element greater than itself

num = int(input("Enter the size of array: "))
list=[]
for i in range(0,num):
    elements = int(input("Enter element: "))
    list.append(elements)

def countGreater(array):
    max = array[0]
    frequency = 0
    for i in range(0,len(array)):
        if array[i] == max:
            frequency += 1
        if array[i] > max:
            max = array[i]
            frequency =1
    return len(array) - frequency
print(countGreater(list))