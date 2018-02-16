# CTI-110 
 # P2HW2 - Tip Tax Total 
 # Your Coogan Daniel
 # Feb/16/2018.

# Get the total cost of meal purchase.
totalCost=float(input("Enter the cost of food : "))
# Calculate .07 sales tax.
tax = totalCost * 0.07
print("the total tax is $",tax)

# Calculate .18 tip.
tip = totalCost *.18 
#Display the cost.
print("the total tip is $",tip)


cost = tax +tip+ totalCost
print("The total cost of meal purchase is $",cost)
