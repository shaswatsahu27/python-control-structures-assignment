# Given list of daily sales
daily_sales = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily_sales:

    # Corrupted data
    if sale == -1:
        print("Corrupted data found. Stopping processing.")
        break

    # No sales day
    elif sale == 0:
        print("No sales today. Skipping.")
        continue

    # Valid positive sales
    else:
        total_sales += sale
        print("Added:", sale, "| Running total:", total_sales)

# Final total
print("Final total sales:", total_sales)
