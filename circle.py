import math

class Circle:
    def __init__(self):
        print("Created!")
    def area(self, l):
        self.line = l
        return self.line ** 2 * math.pi

cir = Circle()

x = int(input("円の半径を入力:"))
print(cir.area(x))

