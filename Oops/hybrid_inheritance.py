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
#Excercise:
class University:
    def __init__(self,uni_name):
        self.university=uni_name
    def ShowDetails(self):
        print(f"The university name is {self.university}")
class Courses(University):
    def __init__(self,course_name,uni_name):
        University.__init__(self,uni_name)
        self.course=course_name
    def ShowDetails(self):
        super().ShowDetails()#The university name is GNIT
        print(f"The university name is {self.university} and course is {self.course}")
class Branch(University):
    def __init__(self, uni_name,branch_name):
        University.__init__(self,uni_name)
        self.branch=branch_name
    def ShowDetails(self):
        super().ShowDetails()
        print(f"The university name is {self.university} and the branch is {self.branch}")
class Student(Courses,Branch):
    def __init__(self, std_name,course_name,branch_name, uni_name):
        Courses.__init__(self,course_name,uni_name)
        Branch.__init__(self,uni_name,branch_name)
        self.student=std_name
    def ShowDetails(self):
        super().ShowDetails()
        print(f"The student is {self.student} from branch {self.branch} and course is {self.course} from {self.university} university")
u=Courses("B-Tech","GNIT")
u.ShowDetails()#The university name is GNIT and course is B-Tech
b=Branch("GNU","AIML")
b.ShowDetails()#The university name is GNU The university name is GNU and the branch is AIML
s=Student("sushma", "B-Tech", "AIML", "KITS")
s.ShowDetails()#The student is sushma from branch AIML and course is B-Tech from KITS university