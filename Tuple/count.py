tple = (7,5,1,3,4,9,7,1,6,)
a= int(input("Enter the number: "))
count=0;
for i in tple:
    if a == i:
        count=count+1
print("count is",count)

print("--------------------------------------")

print(tple.count(a))