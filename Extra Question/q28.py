'''
Write a program to read a list of elements. Input an element from the user that has to be inserted in
the list. Also input the position at which it is to be inserted. Write a user defined function to 
insert the element at the desired position in the list.
'''
def insert(a, indx, val):
    a[indx]=val
    return a

lst = [1,7,1,3,4,4,4,1,3,3,3,9,7,8]
print(insert(lst,1,100))

