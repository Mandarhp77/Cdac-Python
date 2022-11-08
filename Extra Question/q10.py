'''
Python program to capitalize the first and last character of each word in a string
Given the string, the task is to capitalise the first and last character of each word in a string. Examples:

Input: hello world 
Output: HellO WorlD
'''
ip = "hello world"
fop=""

st = list(ip.split(" "))
for i in st:
    i=i.capitalize()
    lent = (len(i)-1)
    fop = fop + i + " "

    last =i[-1]
    lst = last.upper()
 
    fop = fop.replace(last,lst)

print(fop)

