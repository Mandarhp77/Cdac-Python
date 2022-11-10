def max(ls):
    max = 0
    for i in ls:
        if i>max:
            max = i
    return max

lst = [1,-3,5,-7,5,-9,4,-7,9,12]
print(max(lst))