import random
import os

wins=0
loss=0
played=0
print("Wellcome to Rock Paper Scissors.")
while True:
    opt=input("Press E to exit:").upper()
    if opt=="E":
        print("GoodBye")
        break

    RPS=["Rock","Paper","Scissors"]
    randnum=random.randint(0,2)
    comp=RPS[randnum]
    randnum=0
    os.system('cls')
    while randnum not in [1,2,3]:
        print("1.Rock")
        print("2.Paper")
        print("3.Scissors")
        randnum=int(input("Press 1-3 to pick:"))
        if randnum not in [1,2,3]:
            os.system('cls')            
            print("Invalid Input")


    
    player=RPS[int(randnum)-1]
    os.system('cls')
    print("Computer Picked:"+comp)
    print("You Picked:"+player)

    if comp==player:
        print("Draw")
    elif comp=="Rock" and player=="Paper":
        print("You win")
        wins+=1
    elif comp=="Paper" and player=="Scissors":
        print("You win")
        wins+=1
    elif comp=="Scissors" and player=="Rock":
        print("You win")
        wins+=1
    else:
        print("You Lose")
        loss+=1
    
    played+=1
    print("Games Played:"+str(played))
    print("Games won:"+str(wins))
    print("Games Loss:"+str(loss))


