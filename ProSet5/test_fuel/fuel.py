def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    divisor_, dividend_ = fraction.strip().split("/")
    divisor = int(divisor_)
    dividend = int(dividend_)
    if dividend == 0:
        raise ZeroDivisionError
    if type(divisor) is not int or type(dividend) is not int or divisor > dividend or divisor < 0 or dividend < 0:
        raise ValueError
    return round((divisor / dividend) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()