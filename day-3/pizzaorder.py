# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
prize = 0
if size == "S":
    prize += 15
elif size == "M":
    prize += 20
else:
    prize += 25

if add_pepperoni == "Y":
    if size == "S":
        prize += 2
    else:
        prize += 3

if extra_cheese == "Y":
    prize += 1

print(f"Your final bill is: ${prize}")

