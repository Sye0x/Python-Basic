import random

print("Press 1 for Level 1")
print("Press 2 for Level 2")
print("Press 3 for Level 3")
x=int(input("Enter Here:"))
if x==1:
    i=0
    while i<10:
        i=i+1
        operands=["+","-","*","/"]
        pick=random.randint(0,3)
        opt=operands[pick]
        num1=random.randint(0,22)
        num2=random.randint(0,22)
        print(str(num1)+" "+str(opt)+" "+str(num2))
        
    
elif x==2:
    pass
elif x==3:
    pass
else:
    pass







  