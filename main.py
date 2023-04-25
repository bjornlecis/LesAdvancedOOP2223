import abc
class Shape(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def area(self):
      pass
class Rectangle(Shape):
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return self.l*self.b

class Square(Shape):
   def __init__(self,x):
      self.x = x

   def area(self):
      return self.x**2

r = Rectangle(10,20)
s = Square(5)
print ('area: ',r.area())
print ('area: ',s.area())
