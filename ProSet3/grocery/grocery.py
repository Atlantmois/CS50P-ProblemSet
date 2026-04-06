grocery = {}

def main():
        try:
            type()
        except EOFError:
            print()
            for item in sorted(grocery):
                  print(f"{grocery[item]} {item}")

def type():
      while True:
            words = input("").upper()
            if words in grocery:
                  grocery[words] += 1
            else:
                  grocery[words] = 1

main()
