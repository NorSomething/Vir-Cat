import csv
import numpy as np

class Kitty:
    def __init__(self, name, hunger, health, mood):
        self.name = name
        self.hunger = hunger
        self.health = health
        self.mood = mood

cat1 = Kitty("kumar", 0.5, 90, "happy")
cat1Data = [cat1.name, cat1.hunger, cat1.health, cat1.mood]


np.savetxt('data.csv', cat1Data, delimiter='\t',fmt="%s")
dat = np.genfromtxt('data.csv', delimiter=',', dtype=str)

#print(dat)

print("Welcome to Vir-Cat!!")



