name = "the quick brown fox jumps over the lazy dog"

print(name)
print(name.lower())
print(name.upper())


arr =name.split(" ")
arr1=""
for i in arr:
    arr1=arr1+i.capitalize()+" "
print(arr1)


print(arr1.swapcase())
print(name.capitalize())

