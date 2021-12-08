print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names_1_2 = name1.lower() + name2.lower()

t = names_1_2.count('t')
r = names_1_2.count('r')
u = names_1_2.count('u')
e = names_1_2.count('e')

true = t + r + u + e

l = names_1_2.count('l')
o = names_1_2.count('o')
v = names_1_2.count('v')
e = names_1_2.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))


if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}")