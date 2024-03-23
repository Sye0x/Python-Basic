import random

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
        else:
            return score
    
    


def main():
    while True:
        print(dice_roll(2))
        print("Press 1 to play vs Comp")
        print("Press 2 for PVP")
        print("Press E to exit")
        opt=input("Enter Here:").lower()
        if opt=="1":
            pass
        elif opt=="2":
            pass
        elif opt=="e":
            print("GoodBye")
            exit
        else:
            print("Invalid Input")

    

main()