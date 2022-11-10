'''
Consider the following string mySubject:
 mySubject = "Computer Science"
 What will be the output of the following string operations :
'''

mySubject = "Computer Science"
print(mySubject[0:len(mySubject)])
print(mySubject[-7:-1])
print(mySubject[::2])
print(mySubject[len(mySubject)-1])
print(2*mySubject)
print(mySubject[::-2])
print(mySubject[:3] + mySubject[3:])
print(mySubject.swapcase())
print(mySubject.startswith('Comp'))
print(mySubject.isalpha())