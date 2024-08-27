# Write a Python program that asks the user to enter numbers. Keep asking the user to enter a number until they enter a negative number.
# Print the sum of all the numbers entered

def main():
    total_sum = 0

    while True:
        try:
            # Ask the user for a number
            number = float(input("Enter a number (negative number to stop): "))

            # Check if the number is negative
            if number < 0:
                break

            # Add the number to the total sum
            total_sum += number
        except ValueError:
            # Handle invalid input (e.g., if the user doesn't enter a number)
            print("Invalid input. Please enter a valid number.")

    # Print the sum of all the numbers entered
    print(f"The sum of all entered numbers is: {total_sum}")

# Run the main function
if __name__ == "__main__":
    main()

