name = input("Enter the string: ")

res = name.replace(" ", "-")
print(res)

res1=""
for i in name:
    if (i==" "):
        res1 = res1+"-"
    else:
        res1 = res1 + i
else:
    print(res1)
    