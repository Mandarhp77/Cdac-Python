'''
Write a program that contains a function that has one parameter, n, representing an integer
greater than 0. The function should return n! (n factorial). Then write a main function that calls this
function with the values 1 through 20, one at a time, printing the returned results. This is what your
output should look like:
'''
def factrial(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def main(a):
    for i in a:
        print(i,"---",factrial(i))
        
lst=[1,2,3,4,5,6,7,8,9]
main(lst)
