lst = [3,2,5,1,2,1,8]

lst[0],lst[len(lst)-1] = lst[len(lst)-1],lst[0]
print(lst)