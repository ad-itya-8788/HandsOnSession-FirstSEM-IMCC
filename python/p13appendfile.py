#13. Write a Python program to append text to a file and then display its content.

f=open("Aditya.txt","a")
f.write("This is first line\n")
f.close()

f=open("Aditya.txt","r")
print(f.read())
f.close()