'''
Input a string having some digits. Write a function
to return the sum of digits present in this string.
'''

def sum(str):
    sm=0
    for i in str:
        if (i.isalpha()):
            pass
        else:
            sm = sm + int(i)
    return sm

print(sum("mandar1234patil"))
