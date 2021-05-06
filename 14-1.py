class Square:
    square_list = []

    def __init__(self, l):
        self.line = l
        print("Rectangle object created!")
        self.square_list.append((self.line, self.line, self.line, self.line))

    def calculate_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def change_size(self, addw, addh):
        self.width = self.width + addw
        self.height = self.height + addh

    def print_size(self):
        print("{} by {} by {} by {}".format(self.line, self.line, self.line, self.line))

class Compares:
    def __init__(self, var1, var2):
        self.param1 = var1
        self.param2 = var2

square1 = Square(10)
print(Square.square_list)
square1.print_size()

compare1 = Compares(27, 27)
compare2 = Compares(23, 79)

if compare1 is compare1:
    print('True')
else:
    print('False')

if compare1 is compare2:
    print('True')
else:
    print('False')
