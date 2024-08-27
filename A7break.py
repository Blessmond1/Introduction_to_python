#Write a Python program that asks the user to enter numbers. If the user enters a number greater than 100,
# stop the loop using a break statement and print "Loop stopped."

def main():
    while True:
        try:
            # Ask the user for a number
            number = float(input("Enter a number (greater than 100 to stop): "))

            # Check if the number is greater than 100
            if number > 100:
                print("Loop stopped.")
                break
        except ValueError:
            # Handle invalid input (e.g., if the user doesn't enter a number)
            print("Invalid input. Please enter a valid number.")

# Run the main function
if __name__ == "__main__":
    main()



