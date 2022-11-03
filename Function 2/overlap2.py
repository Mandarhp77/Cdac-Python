def overlap(a,b):
    flag=0
    for i in a:
        for j in b:
            if i==j:
                flag=1
                break
            else:
                pass
            
    if flag==1:
        print("yes")
    else:
        print("no")
    
l1 = [1,2,3,4,5]
l2 = [10,6,7,8,9]

overlap(l1, l2)