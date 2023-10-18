print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip /= 100
bill = tip * bill + bill

print("Each person should pay: ${:.2f}".format(round(bill/people, 2)))


