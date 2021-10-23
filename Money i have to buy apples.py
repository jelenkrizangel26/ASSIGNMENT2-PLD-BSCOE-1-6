cash = int(input("Amount of money you have?: "))
apple_price = int(input("How much is an apple?: "))

capacity_to_buy = cash//apple_price
money_change = cash%apple_price

print(f"You can buy {capacity_to_buy} apples and your change is {money_change} pesos.")