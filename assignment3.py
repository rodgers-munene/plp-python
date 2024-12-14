def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Prompt the user to enter the original price
original_price = float(input("Enter the original price of the item: "))
# Prompt the user to enter the discount percentage
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price or the original price if no discount was applied
if final_price == original_price:
    print(f"No discount applied. The price remains: {original_price:.2f}")
else:
    print(f"The final price after applying the discount is: {final_price:.2f}")
