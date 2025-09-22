import random
import numpy as np

class Kitty:

    def __init__(self, name="", hunger=0, health=0, mood=""):
        self.name = name
        self.hunger = hunger
        self.health = health
        self.mood = mood

    def giveAttributes(self):
        self.name = input("Enter the cat's name : ")
        self.hunger = random.randrange(10,50)
        self.health = random.randrange(30,80)
        data = [self.name, self.hunger, self.health]
        np.savetxt('c1Data.csv', data, fmt="%s")
    

print("Welcome to Vir-Cat!!")

choice = int(input("Do you want to create a new cat (1/0)"))
if choice == 1:
    c1 = Kitty()
    c1.giveAttributes()
else:
    exit()




