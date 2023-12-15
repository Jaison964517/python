class Rectangle:
    def __init__(self ,l,b):
        self.length=l
        self.bredth=b

    def area(self):
        Area1=self.length*self.bredth
        return Area1

    def __lt__(self, obj):
        if (self.area() < obj.area()):
           return "The area of Rectangle1 is less than Rectangle2"

        else:
            return "The area of Rectangle2 is less than Rectangle1"


l = int(input("Enter the length of rectangle1:"))
b = int(input("Enter the breadth of rectangle1:"))
obj1=Rectangle(l, b)
print("The area is:")
print(obj1.area())
l = int(input("enter the length o Rect2:"))
b= int(input("enter the bredth of  Rect3:"))
obj2=Rectangle(l, b)
print("The area is:")
print(obj2.area())
print("now compare")
print(obj1<obj2)