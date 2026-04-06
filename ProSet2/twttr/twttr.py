def main():
    text = input("Input: ")
    print("Output:", convert(text))

def convert(str):
    new_str = ""
    vowels = "aeiouAEIOU"
    for char in str:
        if char not in vowels:
            new_str += char
    return new_str

main()
