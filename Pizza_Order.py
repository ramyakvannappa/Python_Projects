print("Welcome to Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

if size == 's':
    price = 15
elif size == 'm':
    price = 20
else:
    price = 25

if add_pepperoni == 'y':
    if size == 's':
       price += 2
    else:
        price += 3

if extra_cheese == 'y':
    price += 1

print(f"Your final bill is: ${price}")
