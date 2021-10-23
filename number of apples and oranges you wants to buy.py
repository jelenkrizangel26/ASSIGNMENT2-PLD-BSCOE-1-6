print("The price of apple is 20 pesos.")
print("The price of orange is 25 pesos")

applesPrice = 20
OrangePrice = 25

quantity_of_apples_to_buy = int(input("How many apples you want to buy?: "))
quantity_of_oranges_to_buy = int(input("How many oranges you want to buy?: "))

amount_of_apples = applesPrice * quantity_of_apples_to_buy
amount_of_oranges = OrangePrice * quantity_of_oranges_to_buy
amount = amount_of_apples + amount_of_oranges

print(f"The total amount is {amount}.")