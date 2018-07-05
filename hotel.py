"""
hotel.py
This is the Hotel class file 
"""

class Hotel():
    hotels = []
    def __init__(self, number,hotel_name, city,total_rooms,empty_rooms):
        self.number = number
        self.hotel_name = hotel_name
        self.city = city
        self.total_rooms = total_rooms
        self.empty_rooms = empty_rooms

    def __repr__(self):
        return f'Hotel({self.number!r}, {self.hotel_name !r},{self.city !r},{self.total_rooms !r},{self.empty_rooms !r})'
       
        
    def check_if_duplicate(self): # check whether hotel is a duplicate or not
        existed= False
        for hotel in Hotel.hotels:
            if hotel.hotel_name == self.hotel_name and hotel.city == self.city:
                existed = True
        return existed

    def add_hotel(self):
        if not self.check_if_duplicate():
            Hotel.hotels.append(self)
            #Hotel.hotels.append([self.number , self.hotel_name, self.city, self.total_rooms,self.empty_rooms])

    def delete_hotel(self):
        for hotel in Hotel.hotels:
            if hotel.hotel_name == self.hotel_name and hotel.city == self.city:
                Hotel.hotels.remove(hotel)  # delete the(list) indicates to specific instance object
                # Hotel.hotels.remove([self.number , self.hotel_name, self.city, self.total_rooms,self.empty_rooms])

def list_hotels_in_city(city):
    hotels_capacity_at_that_city=[]                              #Stand Alone Function 
    hotel_not_in_city=True
    for place in Hotel.hotels:
        if city in place.city:
           hotels_capacity_at_that_city.append([city,place.hotel_name,place.empty_rooms])  
           hotel_not_in_city=False
    if hotel_not_in_city:
        print("we do not have a hotel at that city ")
    return  hotels_capacity_at_that_city                
"""        
initial_version_

class Hotel():
    hotels = []
    def __init__(self, number,hotel_name, city,total_rooms,empty_rooms):
        self.number = number
        self.hotel_name = hotel_name
        self.city = city
        self.total_rooms = total_rooms
        self.empty_rooms = empty_rooms

        Hotel.hotels.append([self.number , self.hotel_name, self.city, self.total_rooms,self.empty_rooms])

    def delete_hotel(self):
        Hotel.hotels.remove([self.number , self.hotel_name, self.city, self.total_rooms,self.empty_rooms])
    
    def list_hotels_in_city(city):                              #Stand Alone Function 
    hotels_city=[]
    hotels_capacity_at_that_city=[]
    for thing in Hotel.hotels:                        # primitive build list includes hotel_names
        hotels_city.append(thing[2])              # primitive
    if city not in  hotels_city:                      # checking the Hotel name
        print("we do not have a hotel at that city ")
    else:
        index_city=[]
        for index_city, j in enumerate(hotels_city):        #locate many indices not only one
            if j == city:
                #print("In "+str(city)+" city "+str(Hotel.hotels[index_city][1])+" Hotel,has "+str(Hotel.hotels[index_city][4])+" available")# was (Hotel.hotels[index_city][2])
                hotels_capacity_at_that_city.append([city,Hotel.hotels[index_city][1],Hotel.hotels[index_city][4]])  
    return  hotels_capacity_at_that_city   
"""
