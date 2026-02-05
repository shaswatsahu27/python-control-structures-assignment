# Read order amount from user
order_amount_input = input("Enter order amount: ")

# Handle non-numeric input
if not order_amount_input.isdigit():
    print("Error: Please enter a valid numeric order amount.")
else:
    order_amount = int(order_amount_input)

    # Apply discount rules
    if order_amount >= 2000:
        discount_rate = 0.15
    elif order_amount >= 1500:
        discount_rate = 0.10
    elif order_amount >= 1000:
        discount_rate = 0.07
    else:
        discount_rate = 0.0

    # Calculate discount
    discount = order_amount * discount_rate
    subtotal = order_amount - discount

    # Extra (optional): Add 5% tax
    tax = subtotal * 0.05
    final_amount = subtotal + tax

    # Print results
    print("Original Amount:", order_amount)
    print("Discount Applied:", discount)
    print("Subtotal after discount:", subtotal)
    print("Tax (5%):", tax)
    print("Final Amount to Pay:", final_amount)
