#Write a Python program to demonstrate single inheritance (Person → Student) andmultilevel inheritance (Person → Student → StudentGraduation) with appropriate attributes.

class person:
  def show(self):
    print("Parant class")
class student(person):
  def study(self):
    print("Student class")
class studgrad(student):
  def degree(self):
    print("Graducation class")
s=studgrad()
s.show()
s.study()
s.degree()