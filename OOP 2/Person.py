class person:
    
    def __init__(self,pid,pname,email,mob):
        self.pid = pid
        self.pname = pname
        self.email = email
        self.mob = mob
        
    def display(self):
        return f"id: {self.pid}, name: {self.pname}, email: {self.email}, mob: {self.mob}"
 
    
class Member(person):
    def __init__(self,pid,pname,email,mob,memtype, amount):
        person.__init__(self, pid, pname, email, mob)
        self.memtype = memtype
        self.amount = amount
        
    def setAmount(self, amount):
        self.amount = amount
    
    def getAmount(self):
        return self.amount
    def display(self):
        return f"{super().display()}, member type: {self.memtype} and amount: {self.amount}"
        
    
class Employee(person):
    def __init__(self,pid,pname,email,mob,dept,desg,salary):
        super().__init__(pid,pname,email,mob)
        self.dept = dept
        self.desg = desg
        self.salary = salary
        
    def setSalary(self,salary):
        self.salary=salary
        
    def getSalary(self):
        return self.salary
    
    def calSalary(self):
        return self.salary + 0.10*self.salary + 0.15*self.salary -0.05*self.salary
        
    def display(self):
        return f"{super().display()} f, dept: {self.dept} designation is {self.desg} salary is {self.salary}"
 

      
obj = Employee("20", "Mandar", "man@123", 8793,"ele","design",20000)
print(obj.display())
print("net salary",obj.calSalary())
print(obj.getSalary())
obj.setSalary(30000)
print(obj.getSalary())

print("--------------------")

ob = Member("20" ,"Aalesh", "aal@123", 8526, "president", 100000)
print(ob.display())
print(ob.setAmount(300000))
print(ob.getAmount())
print(ob.display())




