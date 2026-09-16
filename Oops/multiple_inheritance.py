#Multiple inheritance means having more than one parent class 
class Human:
    def eat(self):
        print("I can eat.")
class Male:
    def flirt(self):
        print("I can flirt.")
class Boy(Human,Male):
    pass
boy_1=Boy()
boy_1.flirt()#I can flirt.
#the boy here is the child or derived class of both human and male.
class Human:
    def eat(self):
        print("I can eat.")
    def work(self):
        print("I can work")
class Male:
    def flirt(self):
        print("I can flirt.")
    def work(self):
        print("I can code")
class Boy(Human,Male):
    pass
boy_1=Boy()
boy_1.work()#I can work 
#in above case there is same method "work" in both parent classes but while calling that method in child class
#it was printing "I can work" not "I can code" this because the order Boy(Human,Male) in this the Human class was first.
#we can printing the Male class work method through below process:
Male.work(boy_1)#I can code

class Human:
    def eat(self):
        print("I can eat.")
    def work(self):
        print("I can work")
class Male:
    def flirt(self):
        print("I can flirt.")
    def work(self):
        print("I can code")
class Boy(Human,Male):
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can test")
    pass
boy_1=Boy()
boy_1.work()#I can test
#if all the classes have same method then the order of selecting and printing is first select the derived class ,then follows the order of the class which at first in derived class.
#this method is called mro:method resolution order.
print(Boy.mro())#[<class '__main__.Boy'>, <class '__main__.Human'>, <class '__main__.Male'>, <class 'object'>]
class Human:
    def eat(self):
        print("I can eat.")
class Male:
    def flirt(self):
        print("I can flirt.")
    def work(self):
        print("I can code")
class Boy(Human,Male):
    def sleep(self):
        print("I can sleep")
boy=Boy()
boy.work()#I can code
#Attribute accessing from parent classes:
class Human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_nose=1
        self.heart=num_heart
    def eat(self):
        print("I can eat")
class Male:
    def __init__(self,name):
        self.name=name
    def sleep(self):
        print("I can sleep")
class Boy(Human,Male):
    def __init__(self,name,heart,language):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.language=language
    def display(self):
        print(f"I'm {self.name},I has {self.num_eyes} eyes and {self.num_nose} nose and i teach {self.language}")
boy=Boy("sushma",1,"Python")
print(boy.num_eyes)#2
print(boy.language)#Python
print(boy.heart)#1
boy.display()#I'm sushma,I has 2 eyes and 1 nose and i teach Python