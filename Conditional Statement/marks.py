marks=int(input("M1: "))+int(input("M2: "))+int(input("M3: "))+int(input("M4: "))+int(input("M5: "))

per = marks/5

if(80<=per<100):
    print("Distinction")
elif(60<=per<80):
    print("A grade")
elif(50<=per<60):
    print("B grade")
elif(0<=per<50):
    print("Fails you fool")

