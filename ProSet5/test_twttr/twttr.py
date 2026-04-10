def main():
    text = input("Input: ")
    print("Output:", shorten(text))

def shorten(str):
    new_str = ""
    # vowels = "aeiouAEIOU"
    vowels = "aeiou"
    for char in str:
        if char not in vowels:
            new_str += char
    return new_str

if __name__ == "__main__":
    main()
