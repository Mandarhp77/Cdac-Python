tple1=(1,2,3,4)
tple2=(5,6,7,8)

print("----1--------------------------")

print(tple1, tple2)

print("----2--------------------------")

tple3 = (tple2+tple1)
print(tple3)

print("----3--------------------------")

print(tuple(list(sorted(tple3))))

#lst = sorted(tple3)
#tple4 = tuple(lst)
#print(tple4)

print("-----4-------------------------")

print(tple3[2])

print("-----5-------------------------")

print(tple3[-3:])

print("-----6------------------------")

print(len(tple3))