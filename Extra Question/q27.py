'''
Write a program to read a list of elements. Modify this list so that it does not contain any duplicate
elements, i.e., all elements occurring multiple times in the list should appear only once.
'''
lst = [1,7,1,3,4,4,4,1,3,3,3,9,7,8]
lst = list(set(lst))
print(lst)
