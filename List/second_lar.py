lst = [-1,2,-6,1,7,1,8,8,8]

lst.sort()
max= max(lst)
smax=0

for i in range(len(lst)-1,0,-1):
    print(i)
    if(i<max):
        smax=i
        break
        
    
print("smax", smax)
    


