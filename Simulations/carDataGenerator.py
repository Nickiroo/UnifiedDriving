#Here are the attributes of the car data set
#- Car ID
#- Dimensions
#- Acceleration curve
#- Top speed
#- Braking intensity
#- Turning radius
#- Color
#- Percentage of speed as it relates to curves
#- Percentage of speed as it relates to hills
#- Percentage of speed as it relates to the speed limit
#- "Wiggle" factor
#- "Wiggle" intensity
#- "Wiggle" frequency


import random
import json

#I want to ask the user if they would like to add a car to the data set
#If they say yes, I want to ask them for the attributes of the car 1 by 1

def askUser():
    print("Would you like to add a car to the data set?")
    answer = input("Type 'yes' or 'no': ")
    if answer == "yes":
        addCar()
    elif answer == "no":
        print("Thank you for using the car data generator!")
    else:
        print("I'm sorry, I didn't understand that.")
        askUser()

def info():
    print("-----------------------------------------------")
    print("-All of the units will be metric.")

def addCar():
    car = {}
    car["Car ID"] = len(cars) + 1
    #ask for the dimensions of the car and store them in a list called dimensions
    dimensions = []
    dimensions.append(input("What is the length of the car? "))
    dimensions.append(input("What is the width of the car? "))
    dimensions.append(input("What is the height of the car? "))
    #Ask if there is a nickname for the car, and if there is, ask for the nickname it in car["Nickname"]
    nickname = input("Is there a nickname for the car? ")
    if nickname == "yes":
        car["Nickname"] = input("What is the nickname for the car? ")
    car["Acceleration curve"] = input("What is the acceleration curve of the car? 1 - slow, 2 - medium, 3 - fast")
    car["Top speed"] = input("What is the top speed of the car? (120 mph = 193 km/h, 60 mph = 96 km/h, 30 mph = 48 km/h etc.)")
    car["Braking intensity"] = input("What is the braking intensity of the car? 1 - slow, 2 - medium, 3 - fast")

    car["Turning radius"] = input("What is the turning radius of the car? (Average turning radius of a car is 12 meters)")
    car["Color"] = input("What is the color of the car? Give a hex code or a color name.")
    car["Percentage of speed as it relates to curves"] = input("What is the percentage of speed as it relates to curves? For example, if the car is going 60 mph and the curve is 30 degrees, the percentage of speed as it relates to curves would be 50%.")
    car["Percentage of speed as it relates to hills"] = input("What is the percentage of speed as it relates to hills? ")
    car["Percentage of speed as it relates to the speed limit"] = input("What is the percentage of speed as it relates to the speed limit? ")
    car["Wiggle intensity"] = input("What is the wiggle intensity of the car? 1-3")
    car["Wiggle frequency"] = input("What is the wiggle frequency of the car? 1-3")
    cars.append(car)
    print("Thank you for adding a car to the data set!")
    askUser()

def save():
    with open("carData.json", "w") as outfile:
        json.dump(cars, outfile)

cars = []
info()
print("-----------------------------------------------")
with open("carData.json") as json_file:
    cars = json.load(json_file)
askUser()
save()
