#parent->child1 ->child2 ->child3.....->child n
'''here the parent class acts as parent for child1 and grandparent for child2 and the child1 acts as parent for child2....so on.
child 2 can inherit attributes and methods from both child1 and parent classes.'''
class Human:
    def eat(self):
        print("I can eat")
class Male(Human):
    def sleep(self):
        print("I can sleep")
class Boy(Male):
    pass
boy=Boy()
boy.eat()#I can eat
boy.sleep()#I can sleep
#
class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def sleep(self):
        print("I can sleep")
    def work(self):
            print("I can code")
class Boy(Male):
    def draw(self):
        print("I can draw")
    def work(self):
        print("I can test")
boy_1=Boy()
boy_1.work()#I can test
print(Boy.mro())#[<class '__main__.Boy'>, <class '__main__.Male'>, <class '__main__.Human'>, <class 'object'>]
#