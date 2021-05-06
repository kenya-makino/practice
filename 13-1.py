class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        print("Rectangle obnect created!")
    def calculate_perimeter(self):
        return (self.width * 2) + (self.height * 2)

class Square:
    def __init__(self, w, h):
        self.width = w
        self.height =  h
        print("Square object created!")
    def calculate_perimeter(self):
        return (self.width * 2) + (self.height * 2)
    def change_size(self, addw, addh):
        self.width = self.width + addw
        self.height = self.height + addh

class Shape:
    def __init__(self):
        print("Shape object created!")
    def what_am_i(self):
        print("I am a shape.")

Rec = Rectangle(12, 8)
Squ = Square(6, 6)

print(Rec.calculate_perimeter())
print(Squ.calculate_perimeter())

#x = int(input("増やしたい横幅:"))
#y = int(input("増やしたい高さ:"))

#Squ.change_size(x, y)

#print(Squ.calculate_perimeter())

class shape_asist(Shape):
    pass

sasist = shape_asist()

sasist.what_am_i()

