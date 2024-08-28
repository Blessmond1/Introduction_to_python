#Write a Python program that takes a list of numbers and returns a new list with only the even numbers from the original list.

def filter_even_numbers(numbers):
    # """
    # Returns a list containing only the even numbers from the given list.
    # """
    # Use a list comprehension to filter out even numbers
    return [num for num in numbers if num % 2 == 0]

def main():
    # Example list of numbers
    numbers = [10, 15, 22, 33, 40, 51, 62, 77]

    # Get the list of even numbers
    even_numbers = filter_even_numbers(numbers)
    
    # Print the result
    print("Even numbers from the list:", even_numbers)

# Run the main function
if __name__ == "__main__":
    main()
