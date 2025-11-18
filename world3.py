import random
from game_engine import slow, ask

def challenge3():
    words = ["python", "escape", "portal", "mystery"]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    slow(f"Unscramble this word: {scrambled}")
    ans = ask("Your answer")
    return ans == word

def hard3():
    words = ["adventure", "dimension", "labyrinth", "challenge"]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    slow(f"HARD MODE: Unscramble this long word: {scrambled}")
    ans = ask("Your answer")
    return ans == word