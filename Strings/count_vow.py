vow="AEIOUaeiou"
count=0
name = input("Enter the string: ")
for i in name:
    if(i in vow):
        count = count+1
else:
    print(count)


