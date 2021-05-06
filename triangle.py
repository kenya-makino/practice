class Triangle:
    def __init__(self):
        self.under = 0
        self.height = 0
        print("Object created!")
    def area(self, u, h):
        self.under = u
        self.height = h
        return self.under * self.height / 2

tri = Triangle()

x = int(input("三角形の底辺を入力:"))
y = int(input("三角形の高さを入力:"))

print(tri.area(x, y))
