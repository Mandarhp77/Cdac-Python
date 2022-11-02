name = input("Enter the string: ")
upper=0
lower=0

for i in name:
    if(i.isupper()):
        upper=upper+1
    elif(i.islower()):
        lower = lower+1
else:
    print(f"upper: {upper}, lower: {lower}")

