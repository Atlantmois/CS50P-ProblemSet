def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <=6:
        return False

    if not s.isalnum():
        return False

    if not s[:2].isalpha():
        return False

    first_digit_index = None
    for i, j in enumerate(s):
        if j.isdigit():
            first_digit_index = i
            break

    if first_digit_index != None:
        if s[first_digit_index] == "0":
            return False

        if not s[first_digit_index:].isdigit():
            return False

    return True

main()
