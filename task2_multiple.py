# Given list of order amounts
orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders = 0

print("Order Amount -> Discount -> Final Amount")
print("------------------------------------------")

# Process each order
for order_amount in orders:

    # Apply discount rules (same as Task 1)
    if order_amount >= 2000:
        discount_rate = 0.15
    elif order_amount >= 1500:
        discount_rate = 0.10
    elif order_amount >= 1000:
        discount_rate = 0.07
    else:
        discount_rate = 0.0

    discount = order_amount * discount_rate
    final_amount = order_amount - discount

    # Count discounted orders
    if discount > 0:
        discounted_orders += 1

    # Add to total revenue
    total_revenue += final_amount

    # Print summary row
    print(order_amount, "->", discount, "->", final_amount)

print("------------------------------------------")
print("Total revenue after discounts:", total_revenue)

# Extra (optional)
print("Number of orders that received discount:", discounted_orders)
