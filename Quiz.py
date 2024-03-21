print("Wellcome To Quiz Game")

ans=input("Will you play my game? ").lower()

if ans!="yes":
    exit()
score=0
print("Okay let's start :)\n")
print("First Question")
ans=input("what come after the number 1: ")
if ans=="2":
    score+=1
    print("Correct")
else:
    print("Incorrect")

print("Second Question")
ans=input("what is 1+1 equal to: ")
if ans=="2":
    score+=1
    print("Correct")
else:
    print("Incorrect")

print("Third Question")
ans=input("what is 3x5 equal to: ")
if ans=="15":
    score+=2
    print("Correct")
else:
    print("Incorrect")

print("Fourth Question")
ans=input("what is 9/3(1+2) equal to: ")
if ans=="1":
    score+=2
    print("Correct")
else:
    print("Incorrect")


print("Your Score is "+str(score))
