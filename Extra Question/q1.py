#Python Program to get Maximum product of elements of list in a 2D list
ip = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
prod = 1
max=0
for i in ip:
    for j in i:
        prod = prod*j
        print(prod)
        if(prod>max):
            max=prod
    prod=1
print(max)

