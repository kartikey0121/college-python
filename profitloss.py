buy=int(input("enter a number"))
sell=int(input("enter a number"))
if (sell == buy):
    print("No profit no loss")
elif (sell>buy):
    print("Profit", sell-buy)
else:
    print("Loss", buy-sell)