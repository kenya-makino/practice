class Horse:
    def __init__(self, name, age, rider):
        self.name = name
        self.age = age
        self.rider = rider

class Rider:
    def __init__(self, name, age, height, weit):
        self.name = name
        self.age = age
        self.height = height
        self.weit = weit

rider = Rider("Jhon smith", 26, 170, 60)

horse = Horse("Thunder bolt", 3, rider)

print(horse.rider.name)
print(horse.rider.age)
print(horse.rider.height)
print(horse.rider.weit)
