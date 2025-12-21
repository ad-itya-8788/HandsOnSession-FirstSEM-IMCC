# Write a Python program to read and print the third line from a file named example.txt. If the file has fewer than three lines, what should your code handle?
fp=open("Aditya.txt","r")
line=fp.readlines()
if len(line)>3:
  print(line[2])
else:
  print("File has less than 3 lines")