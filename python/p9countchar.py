#9. Create a program to count the number of characters in a string provided by the user.
str=input("Enter string:")
count=0
for x in str:
  if x.isalpha():
    count+=1
print("Total Number of chars in string:",count)