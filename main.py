import csv
import numpy as np

class Kitty:

    def __init__(self, name="", hunger=0, health=0, mood=""):
        self.name = name
        self.hunger = hunger
        self.health = health
        self.mood = mood

    def giveAttributes(self):
        self.name = input("Enter the cat's name : ")

#cat1 = Kitty("kumar", 0.5, 90, "happy")
#cat1Data = [cat1.name, cat1.hunger, cat1.health, cat1.mood]


#np.savetxt('data.csv', cat1Data, delimiter='\t',fmt="%s")
#dat = np.genfromtxt('data.csv', delimiter=',', dtype=str)

#print(dat)

print("Welcome to Vir-Cat!!")

choice = int(input("Do you want to create a new cat (1/0)"))
if choice == 1:
    c1 = Kitty()
    c1.giveAttributes()
else:
    exit()



