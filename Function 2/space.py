def correction():
    a="my name is mandar.  my surname is        patil."
 
    a=a.replace(".", ". ")
    a=a.split()
    a=" ".join(a)
    print(a)
    
correction()