# Pet Class Begin =======================================================
class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy +=25
        # print(f'{self.name} is fast asleep!')
        return self
        

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.health -= 15
        return self

    def noise(self):
        return self

class Cat(Pet):
    def __init__(self, name, type, tricks, noise):
        super().__init__(name, type, tricks, noise)
        self.is_king_of_the_jungle = True