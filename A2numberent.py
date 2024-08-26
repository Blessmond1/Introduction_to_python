#Write a Python program that checks if a number entered by the user is positive, negative, or zero, and prints the appropriate message.
number = float(input("enter a number:" ))
if number > 0:
    print("number is positive.")
elif number < 0:
    print("number is negative.")
else:
    print("number is zero.")