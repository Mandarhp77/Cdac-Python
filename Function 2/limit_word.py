def longword(word):
        if(len(word)>6):
            return True
        else:
            return False
        
        
listt = ["mandar","Patil","aalesh","Abhinav"]
fil = list(filter(longword, listt))
print(fil)

print("*"*50)

fil2 = list(filter(lambda word:len(word)>6,["mandar","Patil","aalesh","Abhinav"]))
print(fil2)