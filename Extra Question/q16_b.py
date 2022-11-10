'''Consider the following string myAddress:
myAddress = "WZ-1,New Ganga Nagar,New Delhi"
What will be the output of following string operations :
'''
myAddress = "WZ-1,New Ganga Nagar,New Delhi"

print("lower", myAddress.lower())
print("upper", myAddress.upper())
print("count", myAddress.count('New'))
print("find", myAddress.find('New'))
print("rfind", myAddress.rfind('New'))
print("split", myAddress.split(','))
print("split", myAddress.split(' '))
print("replace", myAddress.replace('New','Old'))
print("partition", myAddress.partition(','))
print("index", myAddress.index('New'))