'''in hierarchical inheritance there are more than one child class inherit the attributes and methods from single parent class'''
class Human:
    def eat(self):
        print("I can eat")
class Male(Human):
    def sleep(self):
        print("I can sleep whole day")
class Female(Human):
    def work(self):
        print("I can work")
female=Female()
female.eat()#I can eat
male=Male()
male.eat()#I can eat
#accessing the attributes:
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def ShowDetails(self):
        print(f"name is {self.name} , age is {self.age}")
    def eat(self):
        print("I can eat")
class Male(Human):
    def __init__(self,name,age,can_dance):
        super().__init__(name,age)
        self.know_dance=can_dance
    def sleep(self):
        print("I can sleep whole day")
class Female(Human):
    def __init__(self, name, age,location):
        Human.__init__(self,name,age)
        self.location=location
    def ShowDetails(self):
        Human.ShowDetails(self)
        print(f"location is {self.location}")
    def work(self):
        print("I can work")
female=Female("susmitha",20,"parkal")
female.eat()
print(female.age)#20
print(female.location)#parkal
female.ShowDetails()#location is Parkal
male=Male("ravi",30,True)
print(male.age)#30
print(male.know_dance)#True