import re


def main():
    print(convert(input("Hours: ")))


def convert(s): 
    if matches := re.fullmatch(
        r"([0-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([0-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)",
        s,
    ):
        # hour_index = [1, 4], minute_index = [2, 5], ampm_index = [3, 6]
        time_list = []
        loop_list = [(matches.group(1), matches.group(2), matches.group(3)), (matches.group(4), matches.group(5), matches.group(6))]
        for hour, minute, ampm in loop_list:
            h = int(hour)
            if ampm == "PM" and h != 12:
                h += 12
            elif ampm == "AM" and h == 12:
                h = 0
            time = f"{h:02}:{minute or "00"}"
            time_list.append(time)
        return f"{time_list[0]} to {time_list[1]}"
    raise ValueError


if __name__ == "__main__":
    main()
