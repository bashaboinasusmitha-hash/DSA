#create class Student and object :
class Student:
    pass
student=Student()#student is object
print(type(student))#<class '__main__.Student'>
#Create a Student class with attributes name and age. Create an object and display the values.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
details=Student("susmitha",20)
print(details.name)#susmitha
print(details.age)#20
#Create a Car class with attributes brand and model. Create two objects with different values and display them.
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
car1=Car("Toyoto","Corolla")
print(car1.brand)#Toyoto
print(car1.model)#Corolla
car2=Car("Mahindra","Scorpio")
print(car2.brand)#Mahindra
print(car2.model)#Scorpio
#default value:
class Instructor:
    followers=0
    def __init__(self,name,address):
        self.name=name
        self.place=address
instructor_1=Instructor("Susmitha","Telangana")
print(instructor_1.name)#Susmitha
print(instructor_1.followers)#0        