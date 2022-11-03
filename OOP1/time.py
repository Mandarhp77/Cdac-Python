class Time:
    
    def __init__(self,h=0,m=0):
        self.h=h
        self.m=m
       
class ftime: 
    
    def add_time(self, t1, t2):
        hr = (t1.h + t2.h)
        mn = (t1.m + t2.m)
        self.t4 = Time(hr,mn)
        
    
    def display_time(self):
        if self.t4.m<60:
            print("Time is: ", self.t4.h,":",self.t4.m)
        else:
            print("Time is: ", self.t4.h+1,":",self.t4.m-60)
        
    def display_min(self):
        print("Minutes are: ", self.t4.m + (self.t4.h*60))
        
        
t1 = Time(5,20)
t2 = Time(5,50)

f = ftime()
f.add_time(t1, t2)
f.display_min()
f.display_time()


        


