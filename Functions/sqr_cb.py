lst=map(int,input("Enter no: ").split())

lst1=list(map(lambda a:[a,a**2,a**3],lst))

print(lst1)