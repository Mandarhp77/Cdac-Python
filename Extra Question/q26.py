'''
Write a program to read a list of n integers and find their median.
Note: The median value of a list of values is the middle one when they are arranged in order. If there
are two middle values then take their average. Hint: You can use an built-in function to sort the list
'''
lst = [1,7,1,3,4,1,3,9,7,8]
lst = sorted(lst)
print(lst)
length = len(lst)
mid = (len(lst)//2)
print(mid)

if(length%2==1):
    print("Median is ",lst[mid])
elif(length%2==0):
    a = (lst[mid] + lst[(mid)-1])/2
    print("Median is ",a)
