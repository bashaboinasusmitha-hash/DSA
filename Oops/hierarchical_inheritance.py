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