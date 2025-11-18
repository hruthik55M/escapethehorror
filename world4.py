import random
from game_engine import slow, ask

def challenge4():
    a, b = random.randint(5, 10), random.randint(2, 5)
    correct = a * b + b
    slow(f"Solve: (a * b) + b where a={a}, b={b}")
    ans = int(ask("Your answer"))
    return ans == correct

def hard4():
    a, b, c = random.randint(2,5), random.randint(5,10), random.randint(1,3)
    correct = (a*b) - c
    slow(f"HARD MODE MATH: Solve (a*b) - c where a={a}, b={b}, c={c}")
    ans = int(ask("Your answer"))
    return ans == correct