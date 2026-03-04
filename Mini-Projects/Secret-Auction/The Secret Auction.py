import art
print(art.logo)
Auction_ongoing=True
Auction={}
def highest_bidder (dictionary_needed):
    winner=""
    highest_bid=0
    max(dictionary_needed)

    for bidder in dictionary_needed :
        bid_amount=dictionary_needed[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The highest bidder is {winner} with {highest_bid}")
while Auction_ongoing==True :
    name=input("Enter a name :")
    bid=int(input("Enter a bid number :"))
    Auction[name]=bid
    print(Auction)
    reply=input("Are there any more bidders? Yes or No :").lower()
    if reply=="no" :
        Auction_ongoing=False
        highest_bidder(Auction)
    elif reply=="yes":
        print("\n "*5)
        print(art.logo)

        


        
