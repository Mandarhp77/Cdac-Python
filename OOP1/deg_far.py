class temp_convert:
    
    def deg_far(self,deg):
        fare = (deg * 1.8)+32
        return fare
        
    def far_deg(self, far):
        degr = (((far-32)*5)/9)
        return degr
    
obj = temp_convert()

print(obj.deg_far(100))

print("%.2f"%obj.far_deg(100))