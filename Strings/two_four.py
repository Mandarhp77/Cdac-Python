name = input("Enter the string: ")
res =""
flag=0
length = len(name)

if length>=2:
    res = res+name[0]
    res = res+name[1]
    res = res+name[length-2]
    res = res+name[length-1]
else:
    print("empty string")
print(res)
