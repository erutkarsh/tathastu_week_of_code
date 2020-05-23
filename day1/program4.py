cost=int(input('Enter the cost price of product'))
sell=int(input('Enter yhe selling price of the product'))
profit=sell-cost
new_sp=(1.05*profit)+cost
print("Profit is",profit)
print("New selling price after 5% profit is",new_sp)
