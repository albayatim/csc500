def calculate_total_meal_cost():
    # Ask the user to enter the charge for the food
    food_charge = float(input("Enter the charge for the food: $"))

    # Calculate the tip amount (18% of the food charge)
    tip_amount = food_charge * 0.18

    # Calculate the sales tax amount (7% of the food charge)
    tax_amount = food_charge * 0.07

    # Calculate the total amount
    total_amount = food_charge + tip_amount + tax_amount

    # Display the amounts
    print(f"Food charge: ${food_charge:.2f}")
    print(f"Tip amount (18%): ${tip_amount:.2f}")
    print(f"Sales tax amount (7%): ${tax_amount:.2f}")
    print(f"Total amount: ${total_amount:.2f}")

# Run the function to calculate the total meal cost
calculate_total_meal_cost()
