class Pet:
# implement __init__( name , type , tricks, noise):
    def __init__(self, name, _type, tricks, noise ):
        self.name = name
        self.type = _type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise
    
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        self.energy -= 15
        return self
# noise() - prints out the pet's sound
    def noise(self):
        print(self.noise)
    
class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self): 
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
            print("Oh no!! You need more pet food!")
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
    
my_treats = ['snausage','bacon','trash bag']
my_pet_food = ['pizza','burger']
    
tobit = Pet("Mr. Tobit","dog", ["tobit on things", "is invisible"], "Hey Hey")
josh = Ninja("Joshua", "Shelby", my_treats, my_pet_food, tobit)
josh.feed()
print(tobit.energy)
print(tobit.health)

