class dealer():
    def __init__(self,did,name,mno,addr):
        self.did=did
        self.name=name
        self.mno=mno
        self.addr=addr
        
    def __str__(self):
        return f"id is{self.did} name is{self.name} mob. No. is{self.mno} address is{self.addr}"
    
addrr=[]
for i in range(2):
    did = int(input("enter id"))
    name = input("enter name")
    mno = input("enter Mob. No.")
    adress = input("enter address")
    addrr.append(dealer(did,name,mno,adress))
    
for i in addrr:
    print(i)
    
for i in addrr:
    if "pune" in i.addr:
        print(i)
        
for i in addrr:
    if i.mno == i.mno[::-1]:
        print(i)