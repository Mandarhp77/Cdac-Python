lst=[1,2,3,4,5,6,7,8,9]

leven=[]
lodd=[]

for i in lst:
    if(i%2==0):
        leven.append(i)
    else:
        lodd.append(i)
        
print(max(leven),"is largest even number")
print(max(lodd),"is largest odd number")

            
