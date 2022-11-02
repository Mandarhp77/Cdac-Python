num = int(input("Enter th number: "))
temp=num
sum=0
while(temp!=0):
    rem = temp%10
    sum = sum+rem
    temp = temp//10
else:
    print("summation of all digit in num is ",sum)
