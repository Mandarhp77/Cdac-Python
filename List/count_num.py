a= int(input())
lst = [-1,2,-6,1,2,1,8]
count=0
for i in lst:
    if i==a:
        count = count +1
print(count)

print("================================")

print(lst.count(a))