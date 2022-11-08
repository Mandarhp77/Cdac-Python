#Program to print duplicates from a list of integers
#Input :  list = [-1, 1, -1, 8]
#Output : output_list = [-1]

ip = [-1, 4,-1,4,1,4,4,-1,-1,8]

newl = []
dup = []

for i in ip:
    if i not in newl:
        newl.append(i)
    else:
        dup.append(i)
print(newl)
print(list(set(dup)))



