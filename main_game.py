import game_engine
from game_engine import slow

from world1 import challenge1, hard1
from world2 import challenge2, hard2
from world3 import challenge3, hard3
from world4 import challenge4, hard4
from world5 import challenge5, hard5


def play_level(name, normal_fn, hard_fn):
    slow(f"\n---- {name} ----")

    if normal_fn():
        slow("✔ Correct! +10 points!")
        game_engine.points += 10
    else:
        slow("✖ Wrong! You must complete HARD MODE to escape!")
        if hard_fn():
            slow("✔ Hard challenge SUCCESS! +5 points!")
            game_engine.points += 5
        else:
            slow("❗ Failed hard mode... but the world forces you out.")
            slow("You escape, but earn NO points.")

    slow("-----------------------------")


def main():
    slow("✨ Welcome to the ESCAPE ROOM MULTIVERSE ✨")
    slow("You must pass through 5 worlds.\n")

    play_level("WORLD 1: Cave of Riddles", challenge1, hard1)
    play_level("WORLD 2: Forest of Numbers", challenge2, hard2)
    play_level("WORLD 3: Lava of Words", challenge3, hard3)
    play_level("WORLD 4: River of Logic", challenge4, hard4)
    play_level("WORLD 5: Final Gate", challenge5, hard5)

    slow("\n🏁 FINAL SCORE 🏁")
    slow(f"Total Points: {game_engine.points}\n")

    if game_engine.points >= 40:
        slow("🌟 GREAT ESCAPE! You mastered the escape worlds!")
    elif game_engine.points >= 20:
        slow("👍 GOOD ESCAPE! You escaped with decent skill.")
    else:
        slow("😅 ROUGH ESCAPE... But you still made it home.")

    slow("\n🏠 You have returned home safely!")
    slow("🎉 GAME COMPLETE 🎉")


main()