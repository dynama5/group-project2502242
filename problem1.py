# Write a function to reverse a string.

# Example:
# Input: "Hello"
# Output: "olleH"

def reverse(str):
  rev=""
  i = 0
  while i < len(str):
    rev+=str[len(str)-i-1]
    i+=1
  print(rev)

reverse("hello")
reverse("helloworld")