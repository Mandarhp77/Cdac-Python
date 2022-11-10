'''
Write a function deleteChar() which takes two parameters one is a string and other is a 
character. The function should create a new string after deleting all occurrences of the 
character from the string and return the new string.
'''
def deleteChar(str, ch):
    str = str.replace(ch, "")
    return str

print(deleteChar("mandar patil kaustubh", "a"))
