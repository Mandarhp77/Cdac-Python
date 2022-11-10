'''
Write a program to read elements of a list.
a) The program should ask for the position of the element to be deleted from the list. Write
a function to delete the element at the desired position in the list.

b) The program should ask for the value of the element to be deleted from the list. Write a
function to delete the element of this value from the list.
'''

def delete(lst,pos):
    lst.pop(pos)
    return lst

lst = [2,1,7,9,3,5,4]
print(delete(lst, 2))

print("*"*20)

def remove(lst,val):
    lst.remove(val)
    return lst

lst = [2,1,7,9,3,5,4]
print(remove(lst, 2))
