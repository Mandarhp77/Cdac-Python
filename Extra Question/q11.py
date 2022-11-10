"""
Python program to check if a string has at least one letter and one number
Given a string in Python. The task is to check whether the string has at least one letter(character) 
and one number. Return “True” if the given string full fill above condition else return “False” (without quotes).
Examples: 

Input: welcome2ourcountry34
Output: True

Input: stringwithoutnum
Output: False
"""

def check(a):
    b=1
    c=0
    for i in a:
        if(i.isdigit()):
            b="z"
            break

    for i in a:
        if(i.isalpha()):
            c="z"
            break
    if(b==c):
        return True
    else:
        return False

ip = "8686"
print(check(ip))
