import inflect
names = []
p = inflect.engine()
while True:
    try:
        name = input("Name: ").strip()
        if name:
            names.append(name)
    except EOFError:
        print()
        break
print("Adieu, adieu, to", p.join(names))
