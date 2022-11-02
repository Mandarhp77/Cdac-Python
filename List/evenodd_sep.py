lst = [3,2,5,1,2,1,8]
even=[]
odd=[]
for i in lst:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even,odd)