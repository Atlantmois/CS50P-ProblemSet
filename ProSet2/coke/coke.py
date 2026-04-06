coke_due = 50
while coke_due > 0:
    print("Amount Due:", coke_due)
    coin = int(input("Insert Coin: "))
    if coin not in [5, 10, 25]:
        continue
    coke_due -= coin
print("Change Owed:", -coke_due)
