import random

class Pet:

    sounds = ["Meow"]
    boredom_threshold = 5
    hunger_threshold = 10
    boredom_decrement = 4
    hunger_decrement = 6

    def __init__(self, name = "kitty"):
        self.name = name
        self.hunger = random.randrange(self.hunger_threshold)
        self.boredom = random.randrange(self.boredom_threshold)
        self.sound = self.sounds[:]

    def clock_tick(self):
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            status = "Happy"
        elif self.hunger > self.hunger_threshold:
            status = "Hungry"
        else:
            status = "Bored"
        
        state = "I am " + self.name + ", and I feel " + status + ". "
        state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sound)
        return state
    

    def teach(self, word):
        self.sound += [word]
        self.reduce_boredom()
    
    def hi(self):
        word = random.choice(self.sound)
        self.reduce_boredom()
        return word
    
    def feed(self):
        self.reduce_hunger()

    
    def reduce_boredom(self):
        self.boredom = max(0,self.boredom - self.boredom_decrement)

    def reduce_hunger(self):
        self.hunger = max(0,self.hunger - self.hunger_decrement)


pet1 = Pet("Nigga")

for i in range(10):
    print(pet1)
    pet1.clock_tick()

for i in range(10):
    pet1.hi()
    print(pet1)

