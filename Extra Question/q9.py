'''
Python program to print even length words in a string
Input: s = "This is a python language"
Output: This is python language
'''

ip = "This is a python language"
temp = list(ip.split(" "))
res = ""
for i in temp:
    if(len(i)%2!=1):
        res = res + i +" "
print(res)

