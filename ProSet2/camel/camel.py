def main():
    camel = input("camelCase: ")
    snake = convert_snake(camel)
    print("snake_case:", snake)

def convert_snake(str):
    blank = ""
    for char in str:
        if char.isupper():
            blank += "_" + char.lower()
        else:
            blank += char
    return blank

main()






"""
def main():
    camel = input("camelCase: ")
    snake = convert_snake(camel)
    print("snake_case:", snake)

def convert_snake(str):
    table = []
    for char in str:
        if char.isupper():
            table.append("_")
            table.append(char.lower())
        else:
            table.append(char)
    return "".join(table)

main()
"""
