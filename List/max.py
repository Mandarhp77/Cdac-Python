lst = [-1,2,-6,1,2,1,8]

max1=lst[0]
for i in lst:
    if(max1<i):
        max1=i
    
print(max1)

print(max(lst))