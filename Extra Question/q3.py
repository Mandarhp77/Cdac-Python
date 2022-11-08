#Sum of number digits in List
#The original list is : [12, 67, 98, 34]
#List Integer Summation : [3, 13, 17, 7]

lst = [12, 67, 98, 34]
sum=0
res=[]
for i in range(0,len(lst)):
    lst[i]=str(lst[i])
    for j in lst[i]:
        sum = sum +int(j)
    print(sum)
    sum = 0
    

    

