import random
from game_engine import slow, ask

def challenge2():
    num = random.randint(1, 10)
    slow("Guess a number between 1–10. You get 3 tries.")
    for _ in range(3):
        guess = int(ask("Enter your guess"))
        if guess == num:
            return True
        elif guess < num:
            slow("Too low!")
        else:
            slow("Too high!")
    return False

def hard2():
    num = random.randint(1, 20)
    slow("HARD MODE: Guess number between 1–20. Only 2 tries.")
    for _ in range(2):
        guess = int(ask("Enter guess"))
        if guess == num:
            return True
    return False