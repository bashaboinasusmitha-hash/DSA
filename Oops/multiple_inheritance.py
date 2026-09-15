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