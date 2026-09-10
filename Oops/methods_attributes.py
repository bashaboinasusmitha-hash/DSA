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