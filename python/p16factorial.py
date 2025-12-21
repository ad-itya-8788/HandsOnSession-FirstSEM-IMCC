#16. Write a recursive function to calculate the factorial of a given number n.
#  What will be the output of factorial(6)?

def fact(n):
  if n==0:
    return 1
  return n*fact(n-1)
print("Factorial of 6 is:",fact(6))