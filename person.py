class Person:
  def __init__(self, name, job=None, pay=0):
    self.name = name
    self.job = job
    self.pay = pay

  def lastName(self):
    return self.name.split()[-1]
  def giveRaise(self, percent):
    self.pay = int(self.pay* (1+percent))

  def __repr__(self):
    return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
  def __init__(self, name, pay):
    Person.__init__(self, name, 'mgr', pay)


  def giveRaise(self, percent, bonus=.10):
    Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
  bob = Person('Bob Smith')
  sue = Person('Sue', job = "dev", pay = 4000)
  print(bob)
  print(sue)
  sue.giveRaise(0.10)
  print(sue)
  tom = Manager('Tom Jones', 50000)
  tom.giveRaise(.10)
  print(tom.lastName())
  print(tom)