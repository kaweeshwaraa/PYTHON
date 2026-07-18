# name = input("What's your name?  \n")
# print("Hello " + name + "\n" + "The number of character in your name is " + str(len(name)))

#day 02 Exercise
print("Welcome to the tip Calculator!")
totalBill = float(input("What was the total bill? $"))
tipAmount = int(input("How much tip would you like to give? 10, 12 , or 15 ?"))
noOfPeople = int(input("How many people to split the bill ?"))
print("Each person should pay " + str(round((totalBill + ((totalBill * tipAmount) / 100)) / noOfPeople, 2)))


