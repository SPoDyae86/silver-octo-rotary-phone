import random
chances = 5
number = random.randint(1,9)
a = int(input("Type a guess here: "))

while chances > 0:
    chances - 1
    if a == number:
        print("Congratulations, you win!")
        break
    elif chances == 1:
        print("You lose! the number was", number)
    elif a != number:
        print("Try again!")
        chances -1
        a = int(input("Type a guess here:"))

   


