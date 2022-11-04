class shape:
    def __init__(self):
        pass
    
    def Area():
        pass
    
class circle(shape):
    def __init__(self,r):
        self.r=r
    
    def Area(self):
        return 3.14*(self.r**2)

class square(shape):
    def __init__(self,s):
        self.s=s
    
    def Area(self):
        return self.s**2
    
class rect(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def Area(self):
        return self.l*self.b    
    
c1=circle(10)
print(c1.Area())
s1=square(10)
print(s1.Area())
r1=rect(10,10)
print(r1.Area())