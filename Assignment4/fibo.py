# Get the number of terms in the Fibonacci series
n = int(input("Enter the number of terms: "))

# Initialize the first two terms
a = 0
b = 1
sum_fib = 0

# Calculate the sum of Fibonacci series using for loop
for i in range(n):
    sum_fib += a
    a = b
    b = a + b

# Output the sum
print(f"The sum of the Fibonacci series is: {sum_fib}")
