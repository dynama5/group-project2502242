# Write a function to check if a number is even.

# Example:
# Input: 4
# Output: True

def isEven(num):
    output = "even" if num % 2 == 0 else "odd"
    print(output)

isEven(2)
isEven(7)
isEven(0)
isEven(-220)
isEven(-777777777)