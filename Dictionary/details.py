detail = {"mandar":"2020","aalesh":"3030","pandu":"5050"}

# Update the value
detail["mandar"]=123456
print(detail)


# Add new entry
detail.update({"pintu":"delhi"})
print(detail)


# print the none while missing keys
print(detail.get("alex"))


# print value for specific key
print(detail["aalesh"])


# print all keys
for i in detail:
    print(i)
    
print(detail.keys())
    
    
# print all values
for j in detail.values():
    print(j)
    
    print(detail.values())
    




