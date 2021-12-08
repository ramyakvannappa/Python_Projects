def prime_checker(number):
    is_prime = True
    if number == 2:
        print(f"{number} is a prime number")
    else:
        for n in range(2, number):
            if number % n == 0:
                is_prime = False

    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


num_to_check = int(input("Check if this is a prime number \n"))
prime_checker(num_to_check)