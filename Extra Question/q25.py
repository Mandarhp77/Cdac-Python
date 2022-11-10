'''
Write a function to return the second largest number
from a list of numbers.
'''

ls= [1,-3,5,-7,5,-9,4,-7,9,12]

ls=list(set(ls))
ls = sorted(ls)
print(ls[-2])