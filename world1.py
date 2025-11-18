from game_engine import slow, ask

def challenge1():
    slow("RIDDLE: I speak without a mouth and hear without ears. What am I?")
    ans = ask("Your answer")
    return "echo" in ans

def hard1():
    slow("HARD MODE RIDDLE: What has keys but can’t open locks?")
    ans = ask("Your answer")
    return "piano" in ans