import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        attempt = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while attempt < 3:
            try:
                answer = int(input(f"{x} + {y} = ").strip())
                if answer != x + y:
                    raise ValueError
                score += 1
                break
            except ValueError:
                print("EEE")
                attempt += 1
                pass
        if attempt == 3:
            print(f"{x} + {y} = {x + y}")
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level not in[1, 2, 3]:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
