n=5
for i in range(n):
  num=1
  print(" "*(n-i-1),end=" ")
  for j in range(i+1):
    print(num,end=" ")
    num=num*(i-j)//(j+1)
  print()
print("Pascle traingle")