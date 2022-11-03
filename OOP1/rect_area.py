class rectangle:
    
    def __init__(self,l=1,b=1):
        self.l=l
        self.b=b
    
    def val(self):
        return self.l*self.b
    
r1=rectangle(10,10)
print(r1.val())