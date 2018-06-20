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

        Hotel.hotels.append([self.number , self.hotel_name, self.city, self.total_rooms,self.empty_rooms])

    def delete_a_hotel(self):
        Hotel.hotels.remove([self.number , self.hotel_name, self.city, self.total_rooms,self.empty_rooms])
        
