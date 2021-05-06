class Apple:
    def __init__(self, c, h, w, p):
        self.color = c
        self.height = h
        self.width = w
        self.place = p
        print("Created!")

apple = Apple("red", 10, 12, "Japan")
print(apple)
