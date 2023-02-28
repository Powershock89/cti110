# This program calculates and displays travel expenses
# February 26, 2023
# CTI-110 P1HW2 - Travel Expense
# Corey Ocampo
#


print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter budget: "))
print()
name = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
accomodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Lastly, how much do you need for food? "))
print()
print("-"*12,"Travel Expenses", 12*'-')
print("Location:        ", name)
print("Initial Budget:   $" + str(budget))
print("Fuel:             $" + str(gas))
print("Accomodation:     $" + str(accomodation))
print("Food:             $" + str(food))
balance = budget - gas - food - accomodation
print("-"*41)
#print("Remaining Balance: ", balance)
print()
print("Remaining Balance: $", format(balance,',.0f'))

