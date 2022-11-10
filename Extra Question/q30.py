'''
Write a program to input your friend’s, names and their phone numbers and store them in the dictionary as the
key-value pair. Perform the following operations on the dictionary:
a) Display the Name and Phone number for all your friends.
b) Add a new key-value pair in this dictionary and display the modified dictionary.
c) Delete a particular friend from the dictionary
d) Modify the phone number of an existing friend
e) Check if a friend is present in the dictionary or not
f) Display the dictionary in sorted order of names
'''
dct = {"mandar":58799, "pandu":16848, "pintu":921566, "chintu": 1815658}

for i,j in dct.items():
    print(f"name: {i}  contact_no {j}")

print("*"*50)

dct["mohit"] = 51266
print(dct)

print("*"*50)

dct.pop("chintu")
print(dct)

print("*"*50)

dct["pintu"] = 222222222
print(dct)

print("*"*50)

name = "mandddar"
if name in dct:
    print(f"the name {name} is present")
else:
    print(f"the name {name} is not present")

print("*"*50)
d={}
lst = []


lst = sorted(dct.keys())
for i in lst:
    d[i]=dct[i]
print(d)

