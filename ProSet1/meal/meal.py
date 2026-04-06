def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    if 12 <= time <= 13:
        print("lunch time")
    if 18 <= time <= 19:
        print("dinner time")



def convert(time):
    h, m = time.split(":")
    result = int(h) + (int(m) / 60)
    return result

if __name__ == "__main__":
    main()
