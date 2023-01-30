from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bids = {}
repeat = True 

def find_highest_bidder(bidder_record):
  highest_bid = 0
  winner = ""
  for bidder in bidder_record:
    if bidder_record[bidder] > highest_bid:
      highest_bid = bidder_record[bidder]
      winner = bidder
  print(f"The highest bidder is {winner} and bidder amount is ${highest_bid}")
  
while repeat:
  name  = input("Enter the name of the bidder :")
  price = int(input("Enter the bid price : $ "))
  bids[name] = price
  new_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
  if new_bidder == "no":
    repeat = False
    find_highest_bidder(bids)  
  elif new_bidder == "yes":
    clear()
    
  
    
