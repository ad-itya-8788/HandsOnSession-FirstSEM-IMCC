#14. Implement a function to check whether a string is a palindrome.

def palindrom(str):
  return str==str[::-1]
str=input("Enter String:")
if palindrom(str):
  print("String is Palindrom")
else:
  print("String is not palindrom")