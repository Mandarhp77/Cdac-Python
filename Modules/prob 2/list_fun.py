def display(a):
        print(a)
        
def reverse(a):
    print(a[::-1])
    
def alternate(a):
    print(a[::2])
    
def upp(a):
    b=[]
    for i in a:
        b.append(i.upper())
    print(b)
        
def low(a):
    b=[]
    for i in a:
        b.append(i.lower())
    print(b)
    
def unique(a):
    b = list(set(a))
    print(b)
    
def duplicate(a):
    b=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                b.append(a[i])
                
    print(list(set(b)))