def gcd(a,b):
  while b!=0:
    a,b=b,a%b
  return a
print("Gcd is:",gcd(24,18))
