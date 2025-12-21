#25.Create a class Person with a constructor to initialize name and age. Add a method to display these details and another method to check if the person is an adult (age 18 or above).
class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def show(self):
    print(self.name,self.age)
  def adult(self):
    return self.age>=18
p=person("ram",20)
p.show()
print("Adult:",p.adult())