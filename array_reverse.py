#Reverse an array

array=[]
num = int(input("enter number of elements:"))
for i in range(0,num):
    elements = int(input("enter element: "))
    array.append(elements)

def arrReverse(A,B):
    for i in range(0,int(A/2)):
        temp = B[i]
        B[i]=B[A-i-1]
        B[A-i-1] = temp
    return B

print(arrReverse(num,array))

#   Alternative method using two pointer approach


def revarr(arr):
    p1 =0
    p2 =len(array) -1
    while p1<p2:
        temp = arr[p1]
        arr[p1] = arr[p2]
        arr[p2] = temp
        p1 +=1
        p2 -=1
    return arr
    
print(revarr(array))

# without using temp variable

def reverseArray(a):
    n = len(a)
    for i in range(0,int(n/2)):
        addn = a[n-1-i] + a[i]
        a[i] = addn - a[i]
        a[n-1-i] = addn - a[i]
    return a
