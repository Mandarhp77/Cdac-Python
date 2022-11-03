def overlap(a,b):
    flag=0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                flag=1
            else:
                pass
            
    if flag==1:
        print("yes")
    else:
        print("no")
    
l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9]

overlap(l1, l2)



