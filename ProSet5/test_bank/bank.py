def main(): 
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")
   

def value(word):
    word = word.lower()
    if word.startswith("hello"):
       return 0
    elif word.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()