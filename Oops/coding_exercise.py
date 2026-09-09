#find the area and circumference of a circle:
class Circle:
    def __init__(self,radius,pie):
        self.radius=radius
        self.pie=pie
    def area(self):
        ans=self.pie*self.radius**2
        print(f"The area of circle is {ans}")
    def circumference(self):
        res=2*self.pie*self.radius
        print(f"The circumference of a circle is {res}")
circle=Circle(4,3.14)
circle.area()#The area of circle is 50.24
circle.circumference()#The circumference of a circle is 25.12
#method - 2:
class Circle:
    pi=3.14
    def __init__(self,r):
        self.radius=r
        self.area=Circle.pi*r*r
        self.circumference=2*Circle.pi*r
circle1=Circle(4)
print(f"The circumference of a circle is {circle1.circumference}")#The circumference of a circle is 25.12
print(f"The area of a circle is {circle1.area}")#The area of a circle is 50.24
#method 3 with return statemnt and methods:
class Circle:
    pi=3.14
    def __init__(self,r):
        self.radius=r
    def circumference(self):
        return 2*Circle.pi*self.radius
    def area(self):
        return Circle.pi*self.radius*self.radius
circle_1=Circle(6)
print(f"The circumference of a circle is {circle_1.circumference()}")#The circumference of a circle is 37.68
print(f"The area of a circle is {circle_1.area()}")#The area of a circle is 113.03999999999999