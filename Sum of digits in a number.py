# Ask the user to enter a number (as a string so we can loop through digits)
num = input("Enter a number: ")

# Initialize a variable to hold the sum of the digits
total = 0

# Loop through each character (digit) in the string
for digit in num:
    # Convert the character to an integer and add it to the total
    total += int(digit)

# Print the final result — the sum of all digits
print("Sum of digits:", total)