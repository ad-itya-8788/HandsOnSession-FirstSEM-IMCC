#Write a Python program to count the number of lines in a file named data.txt. What function is used to read all lines of a file at once?

f=open("Aditya.txt","r")
line=f.readlines()
f.close()
print("Lines are:",line)
print("Total lines is:",len(line))