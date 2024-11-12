

total_selling_price = float(input("Enter the total selling price of 15 items: "))
total_profit = float(input("Enter the total profit earned on 15 items: "))


total_cost_price = total_selling_price - total_profit


cost_price_per_item = total_cost_price / 15

# Display the result
print(f"The cost price of one item is: {cost_price_per_item:.2f}")
