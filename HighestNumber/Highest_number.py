numbers = input("enter all the numbers with a space \n")
numbers_lst = numbers.split()
print(numbers_lst)

for n in range(0, len(numbers_lst)):
    numbers_lst[n] = int(numbers_lst[n])
print(numbers_lst)

highest_num = 0
for number in numbers_lst:
    if number > highest_num:
        highest_num = number
print(f"The highest number in this list is {highest_num}")