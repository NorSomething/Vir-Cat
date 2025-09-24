import random
import csv
import numpy as np
import os

class Kitty:

    def __init__(self, name="", hunger=0, health=0, gender="", mood=""):
        self.name = name
        self.hunger = hunger
        self.health = health
        self.gender = gender
        self.mood = mood

    def giveAttributes(self):
        self.name = input("Enter the cat's name : ")
        self.hunger = random.randrange(10,50+1)
        self.health = random.randrange(30,80+1)
        self.mood = "neutral"
        x = random.randrange(1,2+1)
        if x == 1:
            self.gender = "male"
        elif x == 2:
            self.gender = "female"
        data = [self.name, self.hunger, self.health, self.gender, self.mood]
        np.savetxt('c1Data.csv', data, fmt="%s")
    
    def getAttributes(self):
        with open('c1Data.csv') as d:
            line = [l.strip() for l in d.readlines()]  # removes \n from each line

        print("Name of your cat is :", line[0])
        print(f"Your cat's hunger bar is {line[1]} percent full.")
        print(f"Your cat has {line[2]} health remaining.")
        print(f"Your cat is currently in {line[4]} mood")
        print(f"Your cat's gender is", line[3])

    def main(self):
        while(True):
    
            print("Welcome back user!")
            print("1 to check your kitty's status.")
            print("2 to feed it food.")
            print("3 to check on your cat's health.")
            print("4 to play with your cat.")
            print("5 to exit.")

            i = int(input("Enter your choice : "))

            if i == 1:
                c1.getAttributes()
            elif i == 2:
                c1.feedFood()
            elif i == 4:
                c1.playCat()
            elif i == 5:
                exit()

    def playCat(self):
        #minigame hmmm
        print("Minigame!!")
        ans = input("What is the capital of Egypt?")
        if ans == 'Cairo' or ans == 'CAIRO' or ans == 'cairo':
            print("Correct!!")
            with open('c1Data.csv', 'r') as f:
                lines = f.readlines()
            lines[4] = 'happy' + '\n'
            with open('c1Data.csv', 'w') as f:
                f.writelines(lines)
        else:
            print("Wrong :((")
            with open('c1Data.csv', 'r') as f:
                lines = f.readlines()
            lines[4] = 'sad'+'\n'
            with open('c1Data.csv', 'w') as f:
                f.writelines(lines)
    
    def feedFood(self):
        #read all lines
        with open('c1Data.csv', 'r') as f:
            lines = f.readlines()

        lines[1] = str(int(lines[1])+20) + "\n"

        #write all lines back
        with open('c1Data.csv', 'w') as f:
            f.writelines(lines)



print("Welcome to Vir-Cat!!")

#checking if csv exists 
if not os.path.exists("c1Data.csv") or os.stat("c1Data.csv").st_size == 0:
    c1 = Kitty()
    c1.giveAttributes()
else:
    c1 = Kitty()
    c1.main()

 









