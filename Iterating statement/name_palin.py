name = input("Enter the name: ")
namer = name

print(namer[::-1])

flag=1

if(name==namer):
    flag=0
elif(name!=namer):
    flag=1

if(flag==0):
    print("Palindrome")
elif(flag==1):
    print("not a palindrome")

