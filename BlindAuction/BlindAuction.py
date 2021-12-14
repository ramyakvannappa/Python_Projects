from os import system, name

# define our clear function
def clear():
    _ = system('cls') # picked up from stack overflow to clear the output screen


bidding_details_lst = []
additional_bidder = True

while additional_bidder:
    name = input("What is your name ?")
    price = int(input("What is your bid $ "))

    individual_bidding_details = {}
    individual_bidding_details["name"] = name
    individual_bidding_details["bidding_price"] = price

    print(individual_bidding_details)
    bidding_details_lst.append(individual_bidding_details)

    continue_bidding = input("Are there other bidders? Type yes or no ").lower()

    if continue_bidding == "yes":
       additional_bidder = True
       clear()
    else:
        additional_bidder = False
        print(bidding_details_lst)
        highest_bidding_price = 0
        winner = ''
        for bidder_info in bidding_details_lst:
            if bidder_info['bidding_price'] > highest_bidding_price:
                highest_bidding_price = bidder_info['bidding_price']
                winner = bidder_info['name']

        print(f"The winner is {winner} with a bid of ${highest_bidding_price}")
