# Write a Python program to demonstrate static and class methods in a Car class, where is_valid_car_model() is a static method and get_total_cars() is a class method

class car:
  total=0
  def __init__(self):
    car.total+=1
  @staticmethod
  def is_valide_model(model):
    return model!=" "
  @classmethod
  def get_total_cars(cls):
    return cls.total
c1=car()
c2=car()
print(car.is_valide_model("BMW"))
print(car.get_total_cars())