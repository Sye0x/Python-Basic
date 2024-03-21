import random
high=0
while high<=0:
    high=input("Enter a Number>0: ")
    high=int(high)

print("Guess a number between 0 and "+str(high))

number=random.randint(1,high)
number=str(number)
guess="-1"
tries=0
while guess!=number:
    tries+=1
    guess=input("Make a guess: ")
    if guess!=number:
        print("Incorrect")
        if guess>number:
            print("Try lower")
        else:
            print("Try Higher")

print("Correct you guessed it right the number was " +guess)
print("It took you " +str(tries)+" tries")


