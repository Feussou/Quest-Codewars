from math import *

def litres(time):
    liters = time * 0.5
    return floor(liters)

#La logique est d'attribuer à la variable liters le temps passé à courir multiplié par 0.5 car pour chaque heure
#Nathan consomme un demi litre d'eau, la librairie math permet l'utilisation de floor afin d'arrondir la varirable
#liters à l'inférieur