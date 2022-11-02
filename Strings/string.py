name = input("Enter the name: ")
age = input("Enter the age: ")
salary = input("Enter the salary: ")

print("Hello %s, Your age is %s, with salary %s" %(name,age,salary))

print("Hello {}, Your age is {}, with salary {}".format(name,age,salary))

print("Hello {0}, Your age is {1}, with salary {2}".format(name,age,salary))

print("Hello {a}, Your age is {b}, with salary {c}".format(a=name,b=age,c=salary))

print(f"Hello {name}, Your age is {age}, with salary {salary}")