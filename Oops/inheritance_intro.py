class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Female:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
female_1=Female()
female_1.eat()#I can eat 
''' in above code the female can also eat and work like human because female is part of human being 
so writing the same code multiple times was increasing the number of lines of code.So inheritance helps in reducing the rewriting the same code,and supports reusability of a code.'''
#inheritance : it is the process if extracting the methods,attributes from its parent classs.
class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Female(Human):
    pass
female=Female()
female.eat()#I can eat
#the child class can also different methods from parent class
class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Female(Human):
    def flirt(self):
        print("I can flirt")
female=Female()
female.eat()#I can eat
female.flirt()#I can flirt
#The derived class can redefine the method that was already in parent class-this process is called as "Method Overriding".
class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Female(Human):
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")
female=Female()
female.eat()
female.work()#I can code
#using super() we can define the same method,attribute in derived class as parent class:
class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Female(Human):
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()
        print("I can code")
female=Female()
female.flirt()#I can flirt
female.work()#I can work ,I can code