# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

both = name1.lower()+name2.lower()

t = both.count("t") 
r = both.count("r")
u = both.count("u")
e = both.count("e")

l = both.count("l")
o = both.count("o")
v = both.count("v")
e = both.count("e")

true = t+r+u+e
love = l+o+v+e

loveconc = (str(true) + str(love))

if int(loveconc) < 10 and int(loveconc) > 90:
    print(f"Your score is {loveconc}, you go together like coke and mentos.")
elif int(loveconc) >= 40 and int(loveconc) <= 50:
    print(f"Your score is {loveconc}, you are alright together.") 
else:
    print(f"Your score is {loveconc}.")