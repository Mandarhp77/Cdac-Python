dic={}
while True:
    print("1: add")
    print("2: update")
    print("3: display")
    print("4: find")
    print("5: delete")
    print("6: exit")
    ch=int(input("enter choice"))
    
    if ch==1:
        a=input("enter key")
        b=input("enter value")
        dic[a]=b
        
    if ch==2:
        a=input("enter key to add value")
        b=input("enter value")
        dic.update({a:b})
        
    if ch==3:
        print(dic)
        
    if ch==4:
        key=input("enter key")
        print(dic[key])
        
    if ch==5:
        keys=input("enter key")
        del dic[key]
                      
    if ch==6:
        break
                            
        
    