from game_engine import slow, ask

def challenge5():
    slow("Which is NOT a programming language?")
    slow("A) Python\nB) Java\nC) HTML\nD) C++")
    ans = ask("Your choice (A/B/C/D)").upper()
    return ans == "C"

def hard5():
    slow("Final Hard Gate: Answer BOTH questions correctly.")

    q1 = ask("1) Is Python a snake AND a language? (yes/no)")
    q2 = ask("2) Binary uses only 0 and 1? (yes/no)")

    return q1 == "yes" and q2 == "yes"