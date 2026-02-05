orders = []

while True:
    print("\nMenu:")
    print("1 - Add order amount")
    print("2 - Show all orders and total after discounts")
    print("q - Quit")

    choice = input("Enter your choice: ")

    # Quit the program
    if choice == "q":
        print("Exiting program...")
        break

    # Add order amount
    elif choice == "1":
        amount_input = input("Enter order amount: ")

        if not amount_input.isdigit():
            print("Invalid amount. Please enter a number.")
            continue

        orders.append(int(amount_input))
        print("Order added successfully.")

    # Show orders and totals
    elif choice == "2":
        if len(orders) == 0:
            print("No orders available.")
            continue

        total = 0
        print("\nOrder Amount -> Discount -> Final Amount")
        print("---------------------------------------")

        for order_amount in orders:
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
            total += final_amount

            print(order_amount, "->", discount, "->", final_amount)

        print("---------------------------------------")
        print("Total after discounts:", total)

    # Invalid menu option
    else:
        print("Invalid choice. Try again.")
        continue
