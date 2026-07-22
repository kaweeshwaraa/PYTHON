import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '?', '/', '~', '`']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the WORLD GREATEST GENERATOR")
no_of_letters = int(input("How many letters would you like in your password? "))
no_of_symbols = int(input("How many symbols would you like in your password? "))
no_of_numbers = int(input("How many numbers would you like in your password? "))

password = ""
for i in range(no_of_letters):
    password = password + random.choice(letters)

for i in range(no_of_symbols):
    password = password + random.choice(symbols)

for i in range(no_of_numbers):
    password = password + random.choice(numbers)


print(f"You Super Secure Password is (don't tell anyone): {password}")