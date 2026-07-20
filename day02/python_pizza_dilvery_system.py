print("Welcome to the pizza dilvery system")
size = input("What size pizza do you want? S, M or L:")
pepperoni = input("Do you want a pepperoni? Y or N:")
extra_cheese = input("Do you want extra cheese? Y or N:")
total_bill = 0

if size == "S":
    if pepperoni == "Y":
        total_bill = 15 + 2
    elif pepperoni == "Y" and extra_cheese == "Y":
        total_bill = 15 + 2 + 1
    elif pepperoni == "Y" and extra_cheese == "N":
        total_bill = 15 + 2

elif size == "M":
    if pepperoni == "Y":
        total_bill = 20 + 3
    elif pepperoni == "Y" and extra_cheese == "Y":
        total_bill = 15 + 3 + 1
    elif pepperoni == "Y" and extra_cheese == "N":
        total_bill = 15 + 3

elif size == "L":
    if pepperoni == "Y":
        total_bill = 25 + 3
    elif pepperoni == "Y" and extra_cheese == "Y":
        total_bill = 15 + 3 + 1
    elif pepperoni == "Y" and extra_cheese == "N":
        total_bill = 15 + 3

else:
    print("\n Sorry, you have to choose either S , M or L \n")

print(f"Your total bill is ${total_bill}")




