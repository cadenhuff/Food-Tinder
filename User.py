import getdata
class User:
    ranked_resturants = []
    def __init__(self,location,preference,distance,allergies,price,time):
        self.location = location
        self.preference = preference
        self.distance = distance
        self.allergies = allergies
        self.price = price
        self.time = time

    
    def get_restaurant(self):
        x = getdata.get_restaurants(self.location,self.distance,self.price)
        return x



