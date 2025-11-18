import time

points = 0

def slow(t):
    for ch in t:
        print(ch, end='', flush=True)
        time.sleep(0.02)
    print()

def ask(msg):
    return input(msg + "\n> ").strip().lower()