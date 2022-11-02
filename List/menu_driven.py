lst=[]
while(True):
    print("1: accept elements")
    print("2: Display elements")
    print("3: Insert with index")
    print("4: Remove elements")
    print("5: remove by position ")
    print("6: ascending order")
    print("7: descending order")
    print("6: reverse order")
    print("9: exit")
    val = int(input("Enter choice: "))
    
    if(val == 1):
        a = input("Enter the elements: ")
        lst.append(a)
        
    if(val == 2):
        print(lst)
        
    if(val == 3):
        indx = int(input("Enter the index: "))
        value = input("Enter the Value: ")
        lst.insert(indx, value)
    
    if(val == 4):
        rem = input("Enter the Value: ")
        lst.remove(rem)
        
    if(val == 5):
        rempos = int(input("Enter the position: "))
        lst.pop(rempos)
        
    if(val ==6):
        lst.sort()
        
    if(val ==7):
        lst.sort()
        lst.reverse()
    
    if(val ==8):
        lst.reverse()
    
    if(val ==9):
        break
      
        
        
        
    
    
        
    
    
        
    
  
