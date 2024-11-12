n = 27890
sum = 0
r = 1

while n != 0:
    dig = n % 10  # Extract the last digit
    n = n // 10   # Remove the last digit from n

    # Process the digit
    if dig % 2 == 0:
        dig += 2
        if dig == 10:
           dig = 0
           if dig == 10:
             dig = 0
           
    else:
        dig += 1
        if dig == 10:
           dig = 0
           if dig == 10:
              dig = 0

    # If the digit becomes 10, set it to 0
   

    # Add the modified digit in the correct position
    sum = sum + dig * r
    r = r * 10

# Print the final result after the loop
print(sum)
