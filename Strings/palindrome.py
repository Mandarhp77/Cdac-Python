name = input("Enter the string: ")

rev = name[::-1]

if(name==rev):
    print("Palindrome")
else:
    print("not a palindrome")