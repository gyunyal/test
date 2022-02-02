import random
num = random.randint(1, 10)
name_user = input(" Please, input your name: ")
guest_number = int(input("Guess the number: "))
if guest_number == num:
    print(f"Congratulations {name_user}!  Your number {guest_number} is correct.")
else:
    print(f"Sorry {name_user}, this is not the number! The correct number is {num}.")



