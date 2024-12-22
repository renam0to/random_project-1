import time

def fifty():
    for i in range (1,51):
        time.sleep(0.05)
        print(f"\rITS... {i}%", end="")
    print("\nFifty..!!")

def onehun():
    for z in range (1,101):
        time.sleep(0.05)
        print(f"\rITS... {z}%", end="")
        
    print("\nONE HUNDRED!!!")
loop = True

while loop == True:
    hi = input("\nCHOOSE (1,2,3)~~> ")
    if hi.lower() == "2":
        onehun()
        w = input("'ENTER' TO CONTINUE")

    elif hi.lower() == "3":
        fifty()
        l = input("'ENTER' TO CONTINUE ")

    elif hi.lower() == "1":
        print("WRONG")
        break

    else:
        print("INVALID GRRR")
        continue