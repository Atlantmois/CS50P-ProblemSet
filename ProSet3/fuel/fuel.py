def main():
    while True:
        try:
            divide = (convert(input("Fraction: ")))
            break
        except (ValueError, ZeroDivisionError):
            pass
    if divide <= 1:
        print("E")
    elif divide >= 99:
        print("F")
    else:
        print(f"{divide}%")

def convert(origin):
    num, deno = (origin.split("/"))
    result = round((int(num) / int(deno)) * 100)
    if 0 <= result <= 100:
        return result
    else:
        raise ValueError

main()
