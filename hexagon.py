class Hexagon:
    def __init__(self):
        print("Object created!")
    def calculate_perimeter(self, l):
        self.line = l
        return self.line ** 6

hex = Hexagon()
x = int(input("一辺の長さを入力:"))

print(hex.calculate_perimeter(x))
