
class rec: pass

pers1 = rec()
pers1.name = 'bob'
pers1.job = ['dev', 'mgr']
pers1.age = 40.5


rec.name = 'Bob'
rec.age = 40
print(rec.name)

x = rec()
y = rec()
print(x.name, y.name)
(print(list(rec.__dict__.values())))

class FirstClass:
  def setdata(self, value):
    self.data = value
  def display(self):
    print(self.data)

class SecondClass(FirstClass):
  def display(self):
    print("Current value %s" % self.data)

class ThirdClass(SecondClass):
  def __init__(self, value):
    self.data = value
  def __add__(self, other):
    return ThirdClass(self.data + other)
  def __str__(self):
    return "[ThirdClass: %s]" % self.data
  def __mul__(self, other):
    self.data *= other

# a = ThirdClass('abs')
# a.display()
# print(a)

# z = SecondClass()
# z.setdata("Altay")
# z.display()

# x = FirstClass()
# x.setdata("Hello")
# x = SecondClass()
# x.setdata("Hello")
# x.display()



def uppername(obj):
  return obj.name.upper()

rec.method = uppername


print(x.method())


class Person:
  def __init__(self, name, jobs, age = None):
    self.name = name
    self.jobs = jobs
    self.age = age
  
  def info (self):
    return(self.name, self.jobs)

rec1 = Person('bob', ['dev', 'mgc'], 40.5)
print(rec1.info()) 
