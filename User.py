class User:
    ranked_resturants = []
    def __init__(self,location,preference,distance,allergies,min_price,max_price,time):
        self.location = location
        self.preference = preference
        self.distance = disance
        self.allergies = allergies
        self.min_price = min_price
        self.max_price = max_price
        self.time = time

    
    def get_restaurant(self):
        #Run yelp api to get resturants with params
        



