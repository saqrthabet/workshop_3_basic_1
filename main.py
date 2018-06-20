"""
    main.py
    This is the main application file for the Hotel Reservation system 
"""

from hotel import Hotel    # when you import you will use the file name not the class name
from customer import Customer
from reservation import Reservation
import tester 
from notification import Notifications

show=Notifications()

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
                            
def list_resevrations_for_hotel(hotel_name):
       hotels_names=[]
       list_reservation_for_that_hotel=[]
       hotels=[]
       for thing in Hotel.hotels:                         # primitive build list includes hotel_names
              hotels_names.append(thing[1])              # primitive          
       if hotel_name not in hotels_names:                     # checking the Hotel name
              print ("Sir, please check your spilling once more")
           
       else:
              for item in Reservation.reservations:  # primitive build list includes hotel_names
                     hotels.append(item[0])          # primitive          
              if hotel_name not in  hotels:                      # checking the Hotel name
                     print("we do not have a hotel with that name ")
              else:
                     index_hotel=[]
                     for index_hotel, j in enumerate(hotels):        #locate many indices not only one
                            if j == hotel_name:
                                   #print("In "+str(hotel_name)+" Hotel "+"Customer named under "+str(Reservations.reservations[index_hotel][1])+" booked room number "+str(Reservations.reservations[index_hotel][3]))        
                                   list_reservation_for_that_hotel.append([hotel_name,Reservation.reservations[index_hotel][1],Reservation.reservations[index_hotel][3]])
       return list_reservation_for_that_hotel

"""
Main working platform
"""
tester.start_app()

'''those tests moved to the main.py becuase of contradiction between defining
<import main>&<import tester> in both files tester.py & main.py
'''
#def Test_list_of_available_hotels_in_a_city(city):
show.display("\t Test_list_of_available_hotels_in_a_city('Abu Dhabi')")
show.display(list_hotels_in_city('Abu Dhabi'))
    
#def Test_reservation_in_a_hotel(hotel):
show.display("\t Test_reservation_in_a_hotel('Holydayin')")
show.display(list_resevrations_for_hotel('Holydayin'))


#Conducting Tests // did not workout
#tester.Test_reservation_confirmation()
#tester.Test_reservation_disapproval()
#tester.Test_list_of_available_hotels_in_a_city("Abu Dhabi")  
#tester.Test_reservation_in_a_hotel("Holydayin")   
#tester.Test_misspilled_hotel_name()  
#tester.Test_delete_a_customer()  
#tester.Test_reservation_removal()
