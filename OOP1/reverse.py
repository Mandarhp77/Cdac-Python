class rev():
    def __init__(self,str1):
        self.str1=str1
        
    def revers(self):
        v=self.str1.split()
        v=v[::-1]
        v=" ".join(v)
        return v
    
r1 = rev("I Love My India")
print(r1.revers())