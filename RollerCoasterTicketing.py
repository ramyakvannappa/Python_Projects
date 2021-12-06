print("welcome to the rollercoaster!")
height_ft = float(input("enter your height in ft "))

height_cm = height_ft * 30.48 # ift = 30.48cm

if height_cm >= 120:
    age = int(input("enter your age "))
    if age < 12:
        ride_price = 5
        print(f"Child tickets are ${ride_price}")
    elif age < 18:
        ride_price = 7
        print(f"Youth tickets are ${ride_price}")
    else:
        ride_price = 12
        print(f"Adult tickets are ${ride_price}")

    wants_photo = input("Do you need photos? Y or N ").lower()
    if wants_photo == 'y':
        ride_price += 3
    print(f"Your final price is ${ride_price}")
else:
    print("Sorry, you have to grow taller before you can ride")