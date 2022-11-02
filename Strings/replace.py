name = input("Enter the string: ")
char = input("Enter the charactor: ")

result=""
for i in name:
    if(i==char):
        result = result +"$"
    else:
        result = result+i
    
print(result)

r=name.replace(char, "$")
print(r)