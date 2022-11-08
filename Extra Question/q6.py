'''
Reverse Row sort in Lists of List
The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]
'''

lst1 = [[4, 1, 6], [7, 8], [4, 10, 8]]
tmp=[]
result=[]
for i in lst1:
    tmp = (sorted(i))[::-1]

    result.append(tmp)
    
print(result)

