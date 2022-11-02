a,b,c = input("Numberdal be: ").split(" ")
a=int(a)
b=int(b)
c=int(c)

if(a != b or b != c):
    if(a<b and a<c):
         print("A is smaler")
    elif(b<c):
         print("B is Smaller")
    else:
         print("C is Smaller")
else:
    print("all are equal")
