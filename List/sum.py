lst = [-1,2,-6,1,2,1,8]
sum0=0
sum1=0
sum2=0
for i in lst:
    if(i<0):
        sum0=sum0+i
    elif(i>0 and i%2==1):
        sum1=sum1+i
    else:
        sum2=sum2+i

l1 =[sum0,sum1,sum2]
print(l1)