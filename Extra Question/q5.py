'''
Uncommon elements in Lists of List
The original list 1 : [[1, 2], [3, 4], [5, 6]]
The original list 2 : [[3, 4], [5, 7], [1, 2]]
The uncommon of two lists is : [[5, 6], [5, 7]]
'''

orig1 = [[1, 2], [3, 4], [5, 6]]
orig2 = [[3, 4], [5, 7], [1, 2]]
uncommon = []
common = []

for i in orig1:
    for j in orig2:
        if(i==j):
            common.append(i)
orig1.extend(orig2)
#print(orig1)
print("-------------------")
#print(common)

for i in orig1:
    if i in common:
        pass
    else:
        uncommon.append(i)
print(uncommon)


