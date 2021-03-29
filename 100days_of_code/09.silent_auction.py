logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}
bidding_finished = False


def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ''

  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if int(bid_amount) > int(highest_bid):
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {bidder} is with amount of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = input("What is your bid? $: ")
  bids[name] = price
  should_continue = input("Are there any other bidder? Type 'yes' or 'no'.\n").lower()
  if should_continue == 'no':
    bidding_finished = True
    highest_bidder(bids)
  elif should_continue == 'yes':
    pass
