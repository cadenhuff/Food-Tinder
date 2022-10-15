import pandas as pd
import numpy as np
from User import User

location = input("Enter a Location!") #IDK how this will work in the code, might need to do address
preference = input("What kind of food do you like?") #Could do a ranking 1-5
distance = input("How far are you will to go?")
allergies = input("Do you have any allergies?")
price = input("What price were you considering? Pick one: $,$$,$$$:")
time = input("What time are you thinking of going?")


right_restuarants = []
left_restuarants = []



def main():
    cur_user = User(location,preference, distance, allergies,price,time)

    
    restaurants = cur_user.get_restaurant()
    
    print(restaurants)
    
    






main()
