'''
Python Program to Square Each Odd Number in a List using List Comprehension
data=[1,2,3,4,5,6,7]
[1, 9, 25, 49] 
'''
lit = [1,2,3,4,5,6,7]

res = [i*i for i in lit if i%2==1]
print(res)