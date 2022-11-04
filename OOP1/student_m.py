class Student:
    def __init__(self,rno,sname,course,dict1):
        self.rno=rno
        self.sname=sname
        self.course=course
        self.dist1=dict1
        
    def __str__(self):
        return f"roll no is {self.rno} name is {self.sname} course is {self.course} marks is {self.dist1}"
        
dict12={"hindi":100,"marathi":80}
s1 = Student(12,90,"aa",dict12)
print(s1)

lst=[]
for i in range(1):
    rno=input("Enter No")
    name=input("Enter Name")
    cr=input("Enter Course")
    dict1={input("key"):input("value") for i in range(5)}
    lst.append(Student(rno,name,cr,dict1))
    
for i in lst:
    print(i)
    
