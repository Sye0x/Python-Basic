import random

def dice_roll(score):
    while True:
    
        print("Press 1 to roll the dice")
        print("Press 2 to Stop")
        opt=input("Enter Here:")

        if opt=="1":
            roll=random.randint(1,6)
            print(roll)
            score+=roll
        else:
            return score
    
    

    


def main():
    print(dice_roll(2))
    
main()