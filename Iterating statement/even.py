num1=int(input("Enter Starting point: "))
num2=int(input("Enter Ending point: "))

for i in range(num1, num2+1):
    if(i%2==0):
        print(i, end=" ")
