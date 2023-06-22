# Calculate the square root of a number

# num = int(input("Enter number:"))
# def rootFinder(x):
#     count = 0
#     for i in range(1,x+1):
#         if i*i == x:
#             count +=1
#             return i
#     if count == 0:
#         print("Entry not a perfect square")
# print(rootFinder(num))

num = int(input("enter number: "))


def rootFinder(x):
    i = 1
    ans = 1
    while i*i <= x:
        ans = i
        i += 1
    if ans*ans == x:
        return ans
    else:
        return "Not a perfect square"


print(rootFinder(num))
