import pandas as pd
import numpy as np
<<<<<<< HEAD
import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text = "Hello my name is Eric")

if __name__ == "__main__":
    MyApp().run()

=======
from User import User

location = input("Enter a Location!") #IDK how this will work in the code, might need to do address
preference = input("What kind of food do you like") #Could do a ranking 1-5
distance = input("How far are you will to go?")
allergies = input("Do you have any allergies?")
min_price = input("")
max_price = input("")
time = input("What time are you thinking of going?")


right_restuarants = []
left_restuarants = []



def main():
    cur_user = User(location,preference, distance, allergies, min_price, max_price

    
    cur_user 
    






main()
>>>>>>> f08d72177260e2fc4ebc892c80d656f62a178702
