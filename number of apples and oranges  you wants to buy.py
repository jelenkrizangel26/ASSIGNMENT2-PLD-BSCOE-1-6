print("The price of apple is 20 pesos.")
print("The price of orange is 25 pesos")

price_of_apple = 20
price_of_orange = 25

quantity_of_apples_to_buy = int(input("How many apples you want to buy?: "))
quantity_of_oranges_to_buy = int(input("How many oranges you want to buy?: "))

amount_of_apples = price_of_apple * quantity_of_apples_to_buy
amount_of_oranges = price_of_orange * quantity_of_oranges_to_buy
amount = amount_of_apples + amount_of_oranges

print(f"The total amount is {amount}.")