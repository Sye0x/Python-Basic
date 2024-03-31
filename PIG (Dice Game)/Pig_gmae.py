import random
import os

def dice_roll(score):
    sc=0
    while True:     
        if score+sc >=50:
            return sc   
        print("Press 1 to roll the dice")
        print("Press 2 to Stop")
        opt=input("Enter Here:")
        

        if opt=="1":
            roll=random.randint(1,6)
            if roll==1:
                return 0
            print(roll)
            sc+=roll
        elif opt=="2":
            return sc
        else:
            print("Invalid Input")

def cdice_roll(score,n):
    sc=0
    i=0
    while i<n:
        i+=1
        if score+sc >=50:
            return sc

        roll=random.randint(1,6)
        if roll==1:
                return 0
        
        sc+=roll
    return sc
    
def splayer():
    pscore=0
    cscore=0
    while True:    
        os.system("cls")
        pscore+= dice_roll(pscore)
        print("Player-Score:"+str(pscore))
        os.system("pause")
        os.system("cls")
        
        if pscore<50:
            roll=random.randint(1,6)
            cscore+=cdice_roll(cscore,roll)
            print("System rolls: "+ str(roll)+" timse")
            print("Comp-Score:"+str(cscore))
            os.system("pause")
            os.system("cls")

        if pscore>=50:
            print("Player Wins")
            os.system("pause")
            break
        elif cscore>=50:
            
            print("Comp Wins")
            os.system("pause")
            break

        
         





def main():
    while True:
        os.system("cls")
        print("Press 1 to play vs Comp")
        print("Press 2 for PVP")
        print("Press E to exit")
        
        opt=input("Enter Here:").lower()
        if opt=="1":

            print("\nRULES")
            print("You can roll the Dice till you get a one")
            print("You can add all the score except 1")
            print("if you save the score before getting a one")
            print("the score will be added otherwise")
            print("all the score will be lost\n")
            os.system("pause")
            splayer()

        elif opt=="2":
            pass
        elif opt=="e":
            print("GoodBye")
            break
        else:
            print("Invalid Input")


main()