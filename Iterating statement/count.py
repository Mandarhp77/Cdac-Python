num = int(input("Enter th number: "))
temp=num
count=0
while(temp!=0):
    rem = temp%10
    count = count+1
    temp = temp//10
else:
    print(num,"count of digit is",count)
