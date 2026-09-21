#hybrid imhritance is the combination of different inheritances like it may be combination of single and multiple or multilevel and hierarchical etc.
class A:
    def display(self):
        print("Display from class A")
class B(A):
    def display(self):
        print("Display from class B")
class C:
    def show(self):
        print("Showing details from class C")
class D(B,C):
    def display(self):
        super().display()#Display from class B
        print("Display from class D")
d1=D()
d1.display()# Display from class B ,Display from class D
print(D.mro())#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]
