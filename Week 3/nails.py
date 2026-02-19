# Nail purchase calculator

price_per_nail = 0.10   # 10p = £0.10
postage = 2.00          # Flat postage fee

# Get user input
quantity = int(input("How many nails would you like to buy? "))

# Determine discount rate
if 1 <= quantity <= 50:
    discount_rate = 0
elif 51 <= quantity <= 100:
    discount_rate = 10
elif 101 <= quantity <= 200:
    discount_rate = 20
else:  # 201 or more
    discount_rate = 25

# Calculate costs
cost_before_discount = quantity * price_per_nail
discount_amount = cost_before_discount * (discount_rate / 100)
cost_after_discount = cost_before_discount - discount_amount
total_bill = cost_after_discount + postage

# Display results
print(f"Discount applied: {discount_rate}%")
print(f"Cost before postage and packing: £{cost_after_discount:.2f}")
print(f"Total bill including postage and packing: £{total_bill:.2f}")