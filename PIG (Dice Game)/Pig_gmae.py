import random
import os

def dice_roll(score):
    while True:
    
        print("Press 1 to roll the dice")
        print("Press 2 to Stop")
        opt=input("Enter Here:")
        if score >=50:
            return score


        if opt=="1":
            roll=random.randint(1,6)
            print(roll)
            score+=roll
        elif opt=="2":
            return score
        else:
            print("Invalid Input")

    
    
def splayer():
    pscore=0
    cscore=0
    while True:    
        os.system("cls")
        pscore+= dice_roll(pscore)
        print(pscore)
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