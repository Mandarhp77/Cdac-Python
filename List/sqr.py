lst=[]
for i in range(1,1001):
    if(i%7==0):
        lst.append(i)
print(lst)

print("==================================")

lst = [i for i in range(1,1001) if(i%7==0)]
print(lst)
        