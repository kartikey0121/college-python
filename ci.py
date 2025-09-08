print ("enter principal amount")
prin = int(input())
rate=float(("enter rate "))
time= int(("enetr time period"))
ci = prin*(pow(1+(rate/100), time))-prin
print("compont interset",ci)