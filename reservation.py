

"""
reservation.py
This is the Reservation class file
"""

#from customer import Customer
from hotel import Hotel

global hotels_names


class Reservation():
    reservations=[]                                                 # defined here because, eventually I want an accumulation of the total reservations                                                      
    def __init__(self,hotel_name, customer_name,customer_number):
        self.hotel_name=hotel_name
        self.customer=customer_name
        self.number=customer_number
        #self.message=[]  # if  defined here,in order to have a unique output for each instance object, I get double results
       
    def add_new_reservation(self): # will face a problem if self.message=[]is defined above
        self.message=[]  # defined here,in order to have a unique output for each instance object,this instance variable will be assigned to Notification
        self.room_No=[]
        if reserve_room(self.hotel_name,self.customer):                         # Add hotel_name, customer_name into the reservations list
            self.room_No=Hotel.hotels[index_hotel][4]                           # defining the empty room, which will booked for the customer
            Reservation.reservations.append([self.hotel_name, self.customer, self.number,self.room_No])
            self.message.append(["Confirmation : Customer named under:"+str(self.customer)+" reserved Room.No: "+str(self.room_No)+" at "+str(self.hotel_name)+" Hotel"])
            #Reservation.message.append(["Confirmation : Customer named under:"+str(self.customer)+" reserved Room.No: "+str(Hotel.hotels[index_hotel][4])+" at "+str(self.hotel_name)+" Hotel"])
            return True                                                #add_new_reservation output will be assign to Notification()
            #print("capacity after reservaion");print(Hotel.hotels)
        else:
            print("sorry no rooms available")
            return None
    def delete_a_reservation(self):
        Reservation.reservations.remove([self.hotel_name, self.customer, self.number,self.room_No])  #Hotel.hotels[index_hotel][4] unkown value
        self.room_No+=1         # how to update the No. of empty rooms at Hotel.hotels[index_hotel][4]+=1 
            
def reserve_room(hotel_name,customer_name):
        hotels_names=[]
        for thing in Hotel.hotels:                         # primitive build list includes hotel_names
                hotels_names.append(thing[1])              # primitive
                
        if hotel_name not in hotels_names:                     # checking the Hotel name
            print("Sir,please check your spilling once more")
            return False
        else:                                            # else reserve a new room in hotel_name for customer_name
            global index_hotel
            index_hotel=[]
            index_hotel=hotels_names.index(hotel_name)            #used for 2 purposes: check room availablity and list_reservations_for_hotel
        if Hotel.hotels[index_hotel][4]==0:          # loop and check if there is empty_rooms in hotel_name
            return False
        else:
            Hotel.hotels[index_hotel][4]-=1            # update the empty rooms in hotel_name
            return True



