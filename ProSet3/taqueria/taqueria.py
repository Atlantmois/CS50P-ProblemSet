menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
        total = 0.0
        try:
            while True:
                item = input("Item: ").lower()
                total, found = calculate(item, total)
                if found:
                    print(f"Total: ${total:.2f}")
        except EOFError:
            pass

def calculate(item_name, cost):
    for i in menu:
        if item_name == i.lower():
            cost += float(menu[i])
            return cost, True
    return cost, False

main()         
