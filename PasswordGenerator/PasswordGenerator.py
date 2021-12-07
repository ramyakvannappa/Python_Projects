import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator! ")
num_of_letters = int(input("How many letters would you like in your password? \n"))
num_of_numbers = int(input("How many numbers would you like in your password \n"))
num_of_symbols = int(input("How many symbols would you like in your password \n"))

#print(num_of_letters)
#print(num_of_numbers)
#print(num_of_symbols)

password_lst = []
for char in range(1, num_of_letters + 1 ):
    random_char = random.choice(letters)
    password_lst += random_char


for char in range(1, num_of_numbers + 1 ):
    random_num = random.choice(numbers)
    password_lst += random_num


for char in range(1, num_of_symbols + 1 ):
    random_symbols = random.choice(symbols)
    password_lst += random_symbols
print(password_lst)

random.shuffle(password_lst)
print(password_lst)

password = ""
for char in password_lst:
    password += char
print(f"Your password is {password}")




