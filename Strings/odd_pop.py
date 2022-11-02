name = input("Enter the string: ")
length = len(name)
res=""
for i in range(0,length,2):
    res = res+name[i]
else:
    print(res)

print("==============================")
res1=""    
for i in range(length):
    if i%2!=0:
        res1 = res1+""
    else:
        res1 = res1+name[i]
else:
    print(res1)
    
    
        


