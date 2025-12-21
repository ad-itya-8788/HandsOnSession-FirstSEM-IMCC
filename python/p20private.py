#20.Create a class Student with a private attribute _name. Implement setter and getter methods for the attribute. How would you set the name to "Alice" and then retrieve it?
class Student:
  def setName(self,name):
    self._name=name
  def getName(self):
    return self._name
s=Student()
s.setName("Aditya")
print("My name is:",s.getName())