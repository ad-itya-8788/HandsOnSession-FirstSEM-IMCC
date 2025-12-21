#Write a Python program that reads a text file and prints its content line by line.


fp=open("p7max3.py","r")

for line in fp:
  print(line)

fp.close()