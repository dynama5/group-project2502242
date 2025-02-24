# Write a function to calculate the factorial of a number.

# Example:
# Input: 5
# Output: 120

def factorial(num):
    output = 1
    i = 1
    while i <= num:
        output *= i
        i+=1
    print(output)

factorial(1)
factorial(2)
factorial(4)
factorial(5)
factorial(0)