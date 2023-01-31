# Ninja Class Begin =======================================================
class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        print(f'{self.first_name} walked their {self.pet.type}!')
        return self
    def feed(self):
        self.pet.eat()
        print(f'{self.first_name} fed their {self.pet.type}!')
        return self
    def bathe(self):
        print(f'{self.first_name} bathed their {self.pet.type} and they said {self.pet.noise}!')
        return self
    def is_king(self):
        if self.pet.is_king_of_the_jungle == True:
            print(f'{self.pet.name} is king of the jungle!')
        else:
            print(f"{self.pet.name} isn't king but still pretty cool.")
            return self