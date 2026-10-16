import random

lucky_number = random.randint(1, 100)
a = int(input("Enter a number between 1 and 100: "))
while (a != lucky_number):
    if a > lucky_number:
        print("Your number is too high! Noob")
        a = int(input("Enter a number between 1 and 100: "))
    else:
        print("Your number is too low! Noob")
        a = int(input("Enter a number between 1 and 100: "))
print("Your lucky number is:", a,"NIGGA")   
