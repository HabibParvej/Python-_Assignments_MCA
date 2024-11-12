n = int(input("Enter a number: "))
sum = 0
r = 1

# Special case: Handle input '0'
if n == 0:
    print(0)
else:
    while n != 0:
        dig = n % 10  # Get the last digit
        n = n // 10   # Remove the last digit

        if dig == 0:
            # 0 remains 0
            dig = 0
        elif dig % 2 == 0:
            # Even number, add 2. If it becomes 10, set to 0
            dig += 2
            if dig == 10:
                dig = 0
        else:
            # Odd number, add 1
            dig += 1
            if dig == 10:
                dig = 0

        # Rebuild the number with the modified digit at the correct place
        sum = sum + dig * r
        r = r * 10

    # Finally print the result
    print(sum)
