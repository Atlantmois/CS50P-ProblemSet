month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
        while True:
            try:
                date = input("Date: ").strip()
                if date[0].isdigit():
                    print(convert_1(date))
                else:
                    print(convert_2(date))
            except ValueError:
                 pass
            else:
                 break

def convert_1(date_origin):
    m, d, y = date_origin.split("/")
    m, d, y = int(m), int(d), int(y)
    if not (1 <= m <= 12 and 1 <= d <= 31):
        raise ValueError
    date_converted = f"{y}-{m:02d}-{d:02d}"
    return date_converted

def convert_2(date_origin):
    if "," not in date_origin:
        raise ValueError
    m, d, y = date_origin.replace(",", "").split(" ")
    for index, month_name in enumerate(month_list):
         if m == month_name:
              m = index + 1
              break
    m, d, y = int(m), int(d), int(y)
    if not (1 <= m <= 12 and 1 <= d <= 31):
        raise ValueError
    date_converted = f"{y}-{m:02d}-{d:02d}"
    return date_converted

main()
