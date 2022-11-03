class getprint:
    
    def __init__(self, inputs):
        self.inputs = inputs
    
    def getinputs(self,ip):
        self.inputs=ip
        return self.inputs
    
    def prints(self):
        print(self.inputs.upper())
        
obj = getprint("mandar patil")
obj.getinputs("pintu_chintu")
obj.prints()