class Rectangle:
    def __init__(self,length,breadth):
      self.length = length
      self.breadth = breadth 

    def display(self):
       print("length=", self.length)
       print("breadth=", self.breadth)

    def area(self):
       return self.length * self.breadth

r1= Rectangle(10,5)

r1.display()
print("area=", r1.area())

class box:
    def __init__(self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height

    def display (self):
        print("length=",self.length)
        print("breadth=",self.breadth)
        print("height=",self.height)

    def area(self):
       return 2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.height)

    def volume(self):
       return self.length * self.breadth * self.height

b= box(10,5,4)
b.display()
print("box surface area=",b.area())
print("box volume=",b.volume())

class circle:
     def __init__(self,radius):
          self.radius= radius

     def display(self):
         print("radius=",self.radius)

     def area(self):      
         return 3.14 * self.radius * self.radius

     def circumference(self):
         return 2 * 3.14 * self.radius

c = circle(7)
c.display()
print("circle area =", c.area())
print("circle circumference=",c.circumference())

class BankAccount:
     
     x=1000

     def __init__(self,name,balance=0):
         BankAccount.x += 1
         self.accno=BankAccount.x
         self.name = name
         self.balance = balance

     def display(self):
         print("Account No:", self.accno)
         print("name:", self.name)
         print("balance:",self.balance)

     def deposite(self,amount):
         self.balance += amount

     def withdraw(self,amount):
         if amount <= self.balance:
             self.balance -= amount
         else:
             print("insufficient balance")

a1=BankAccount("john", 5000)
a2=BankAccount("alice",3000)

a1.display()
a1.deposite(1000)
a1.withdraw(2000)

print("after transactions:")
a1.display()

a2.display()