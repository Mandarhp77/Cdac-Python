A=[1,2]
B=[3,4]
'''
for i in range(2):
    A[i] = int(input("Enter elements: "))
    
for i in range(2):
    B[i] = int(input("Enter elements: "))
    '''
for i in A:
    for j in B:
        print((A[i], B[j]))
        
print("----------------------------")

arr1=input().split()
arr2=input().split()
arr3=((i,j) for i in arr1 for j in arr2)
print(arr3)