a={5:8, 9:6}
b={50:80, 90:60}

#two to third dictionary
dictn = {**a,**b}
print(dictn)

#concat between two
for i in a:
    b[i]=a[i]
print(b)