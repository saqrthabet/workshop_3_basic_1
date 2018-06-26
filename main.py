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
       
"""
Main working platform
"""
tester.start_app()

#Conducting Tests // did not workout
#tester.Test_reservation_confirmation()
#tester.Test_reservation_disapproval()
#tester.Test_list_of_available_hotels_in_a_city("Abu Dhabi")  
#tester.Test_reservation_in_a_hotel("Holydayin")   
#tester.Test_misspilled_hotel_name()  
#tester.Test_delete_a_customer()  
#tester.Test_reservation_removal()
