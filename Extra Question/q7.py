'''
Python program to find the sum of a Sublist
The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
result is [11,15,22]
'''
orig = [[4, 1, 6], [7, 8], [4, 10, 8]]
sum=0
result=[]
for i in orig:
    for j in i:
        sum = sum + j
    result.append(sum)
    sum=0
print(result)

