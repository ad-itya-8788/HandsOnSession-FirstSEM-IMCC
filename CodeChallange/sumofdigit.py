def sumofdigit(n):
  if n==1:
    return 0
  return (n%10)+sumofdigit(n//10)

print("Sum of digit of  1234 is",sumofdigit(1234))