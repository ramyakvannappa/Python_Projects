import random

print("Welcome! let's see who is going to pay today's bill")
names = input("Give me everybody's names, separated by a comma. ")
name_lst = names.split(",")
print(name_lst)

random_index = random.randint(0,len(name_lst)-1)
person_who_pays_bill = name_lst[random_index]

print(f"{person_who_pays_bill} is going to buy the meal today! ")