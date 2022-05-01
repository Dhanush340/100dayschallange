print("Welcome to the secret auction program")
bidding = False
bids = {}


def find_highest_bid(bids_list):
    high_bid = 0
    winner = ""
    for bidder in bids_list:
        if bids_list[bidder] > high_bid:
            high_bid = bids_list[bidder]
            winner = bidder
    print(f"winner is {winner} and bid is ${high_bid}")


while not bidding:
    name = input("what is your Name: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    any_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if any_bidders == 'no':
        bidding = True
        find_highest_bid(bids)
    elif any_bidders == "yes":
        bidding = False
