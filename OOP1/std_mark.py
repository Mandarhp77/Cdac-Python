class Student():
    def __init__(self,name="name",rno=0):
        self.name=name
        self.rno=rno
        
    def Display(self):
        print(f"name is {self.name} and roll no is {self.rno}")
        
    def setAge(self,age):
        self.age=age
        
    def setMark(self,mark):
        self.mark=mark

std1=Student("Mandar", 22)

std1.Display()
std1.setMark(100)
std1.setAge(30)
print("age: ",std1.age, "Marks: ",std1.mark)