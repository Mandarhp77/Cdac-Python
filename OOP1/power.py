class power:
    
    def __init__(self,base,index):
        self.base = base
        self.index = index
        
    def power(self):
        return (self.base)**(self.index)
    
    def __del__(self):
        print("mi destructor madhe aahe")
    
obj = power(3,3)
print(obj.power())

del obj

print(obj.power(10,2))

        

        
        