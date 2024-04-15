import time
import random
import os

def cal(num1, num2, opt):
    if opt == "+":
        return num1 + num2
    elif opt == "-":
        return num1 - num2
    elif opt == "*":
        return num1 * num2
    elif opt == "/":
        return num1 / num2

def generate_question(level):
    if level == 1:
        return random.randint(0, 16), random.randint(1, 16), random.choice(["+", "-", "*", "/"])
    elif level == 2:
        return random.randint(0, 128), random.randint(1, 128), random.choice(["+", "-", "*", "/"])
    elif level == 3:
        return random.randint(0, 256), random.randint(1, 256), random.choice(["+", "-", "*", "/"])

def play_level(level):
    i = 0
    correct_answers = 0
    start = time.time()  # Measure the start time for the level
    while i < 10:
        os.system("clear")  # for Unix-based systems, use "cls" for Windows
        i += 1
        num1, num2, opt = generate_question(level)
        ans = cal(num1, num2, opt)
        print(f"Question {i}: {num1} {opt} {num2}")
        try:
            user_ans = float(input("Enter Your Answer: "))
            if ans == user_ans:
                print("Correct")
                correct_answers += 1
            else:
                print("Incorrect")
        except ValueError:
            print("Invalid input. Please enter a number.")
        input("Press Enter to continue...")
    end = time.time()  # Measure the end time for the level
    res = int(end - start)  # Calculate the duration of the level
    os.system("clear")
    print(f"Number of Correct Answers: {correct_answers}")
    print("It took you " + str(res) + " Seconds")

while True:
    os.system("clear")
    print("Press 1 for Level 1")
    print("Press 2 for Level 2")
    print("Press 3 for Level 3")
    level_choice = input("Enter Here:")
    
    if level_choice.isdigit():
        level_choice=int(level_choice)
        if 1 <= level_choice <= 3:
            play_level(level_choice)
        else:
            print("Invalid input. Please enter a number shown.")
            input("Press Enter to continue...")
    else:
        print("Invalid input. Please enter a number shown.")
    input("Press Enter to continue...")
