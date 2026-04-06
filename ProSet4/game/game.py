import random
while True:
    try:
        level = int(input("Level: ").strip())
        if not level < 1:
            break
    except ValueError:
        pass
n = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: ").strip())
        if guess < 1:
            continue
        if guess < n:
            print("Too Small!")
        elif guess > n:
            print("Too Large!")
        else:
            print("Just Right!")
            break
    except ValueError:
        pass

