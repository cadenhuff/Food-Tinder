import pandas as pd
import numpy as np
from User import User

location = input("Enter a Location!") #IDK how this will work in the code, might need to do address
preference = input("What kind of food do you like") #Could do a ranking 1-5
distance = input("How far are you will to go?")
allergies = input("Do you have any allergies?")
min_price = input("")
max_price = input("")
time = input("What time are you thinking of going?")





def main():
    x = User(location,1,2,3,4,5,6)
    print(x.location)





main()
