#Create a Student class with an attribute name and a method that prints:Hello, my name is <name>
class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Hello my name is {self.name}")
detaila=Student("Susmitha")
detaila.display()#Hello my name is Susmitha
#diaplay student name marks and subject:
class Student:
    def __init__(self,name):
        self.name=name
    def display(self,marks,subject):
        print(f"Hello my name is {self.name} and i got {marks} marks in {subject}")
detaila=Student("Susmitha")
detaila.display(35,"Maths")#Hello my name is Susmitha and i got 35 marks in Maths
#Create a Rectangle class with attributes length and breadth. Create a method to calculate and display the area.
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def rect_area(self):
        a=self.length*self.breadth
        print(f"The area of rectangle is {a} square units")
dimensions=Rectangle(10,5)
dimensions.rect_area()#The area of rectangle is 50 square units
#Create a BankAccount class with attributes account_holder and balance. Create methods to:Display account details,Deposit money,Display the updated balance.
class BankAccount:
    def __init__(self,account_holder,balance):
        self.name=account_holder
        self.money_balance=balance
    def display(self):
        print(f"The account holder is {self.name} and the account balance is {self.money_balance}")
    def deposit(self,money):
        self.money_balance+=money
        print(f"The deposit money is {money}")
    def updated_balance(self):
        print(f"The final balance is {self.money_balance}")

details=BankAccount("Susmitha",30000)
details.display()
details.deposit(10000)
details.updated_balance()