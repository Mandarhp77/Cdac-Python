dic = {"a":1, "b":2, "c":3, "d":4, "e":5}

# print the counts
count = len(dic)
print("Count is: ",count)

# print the updates
dic.update({"c":7})
print(dic)

# remove the key
dic.pop("e")
print(dic)

# sort the elements
lst =sorted(dic.keys())
for i in lst:
    print(i,dic[i])