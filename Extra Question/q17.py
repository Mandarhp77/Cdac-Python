'''
1. Write a program to input line(s) of text from the user until enter is pressed. 
Count the total number of characters in the text (including white spaces),
total number of alphabets, 
total number of digits, 
total number of special symbols and total number of
words in the given text. 
(Assume that each word is separated by one space).
'''

#ip = input("Enter the lines: ")
ip = "Mandar Patil25(*&^"

print(f"Total no of charactors are: ",len(ip))

count = 0
for i in ip:
    if(i.isalpha()):
        count = count +1
print(f"Total no of aplhabets are: ",count)

cnt = 0
for i in ip:
    if(i.isnumeric()):
        cnt = cnt +1
print(f"Total no of digit are: ",cnt)

ct = 0
for i in ip:
    if(i.isalnum()):
        pass
    else:
        ct = ct + 1
print(f"Total no of special charactors are: ",ct)

we = ip.split(" ")
print(len(we))
