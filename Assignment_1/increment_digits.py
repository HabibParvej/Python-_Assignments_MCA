


# Input: Five-digit number
number = input("Enter a five-digit number: ")

# Step 1: Initialize an empty string to store the new number
new_number = ""

# Step 2: Process each digit and add 1 (wrap around if digit is 9)
for digit in number:
    new_digit = (int(digit) + 1) % 10  # Add 1 and use modulo to handle 9 -> 0
    new_number += str(new_digit)  # Append the new digit to the new number

# Step 3: Display the new number
print(f"The new number is: {new_number}")