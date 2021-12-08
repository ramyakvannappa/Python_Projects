welcome_msg = "Welcome to the tip calculator"
print(welcome_msg)

bill= float(input("What was the total bill amount? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))

bill_per_person = bill * (1 + tip_percentage * .01) / num_of_people
# rounded_bill_per_person = round(bill_per_person, 2)
rounded_bill_per_person = "{:.2f}".format(bill_per_person) #to round it to 2 decimal places. i.e displays 0 at the 2nd decimal place as well
print(f"Each person should pay: ${rounded_bill_per_person}")



