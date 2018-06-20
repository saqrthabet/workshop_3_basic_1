
"""
tester.py
This is the tester class file 
"""

from hotel import Hotel    # when you import you will use file name not class name
from customer import Customer
from reservation import Reservation
from notification import Notifications
#import main

show=Notifications()

def start_app():
    Rotana_hotel = Hotel(1,"Rotana","Abu Dhabi",200,40)
    Sheraton_hotel = Hotel(2,"Sheraton","Abu Dhabi",300,100)
    Hayat_hotel = Hotel(3,"Hayat","Aden",150,100)
    Crecent_hotel = Hotel(4,"Crecent","Mukala",200,50)
    Holydayin_hotel = Hotel(5,"Holydayin","Sana'a",200,100)
    Zero_hotel = Hotel(6,"Zero","Virtual",200,0)  # used to check unavailablity condition
    
    show.display("\t list of the Hotels available")
    show.display(Hotel.hotels)# Check the General details for all hotels
   
    #Create instance objects for 4 customers 
    Saqr_Thabet=Reservation("Hayat","Saqr_thabet","+8613094449161")
    Ali_Ahmed=Reservation("Holydayin","Ali_ahmed","+8613094449161")
    Ameer_Nezar=Reservation("Holydayin","Ameer_nezar","+8613094449161")
    Galal_Taleb=Reservation("Zero","Galal_taleb","+8613228191565")

    #Create reservations for 4 customers
    if Saqr_Thabet.add_new_reservation():
        s_t=Customer(Saqr_Thabet.hotel_name,Saqr_Thabet.customer,Saqr_Thabet.number)
        show.display(Saqr_Thabet.message)
        #show.display(Saqr_Thabet.reservations)
        show.send_message(Saqr_Thabet.message,Saqr_Thabet.number)
        
    if Ali_Ahmed.add_new_reservation():
        m_a=Customer(Ali_Ahmed.hotel_name,Ali_Ahmed.customer,Ali_Ahmed.number)
        show.display(Ali_Ahmed.message)
        #show.display(Ali_Ahmed.reservations)
        show.send_message(Ali_Ahmed.message,Ali_Ahmed.number)
        
    if Ameer_Nezar.add_new_reservation():
        m_b=Customer(Ameer_Nezar.hotel_name,Ameer_Nezar.customer,Ameer_Nezar.number)
        show.display(Ameer_Nezar.message)
        #show.display(Ameer_Nezar.reservations)
        show.send_message(Ameer_Nezar.message,Ameer_Nezar.number)

#def Test_reservation_disapproval():
    show.display("\t Test_reservation_disapproval ") 
    if Galal_Taleb.add_new_reservation():   # no rooms available 
        m_c=Customer(Galal_Taleb.hotel_name,galal.customer,galal.number)
        #show.display(Galal_Taleb.message)
        #show.display(Galal_Taleb.reservations)
        #m_a1.send_message(Galal_Taleb.message,Galal_Taleb.number)

    
#def Test_misspilled_hotel_name():
    show.display("\t Test_misspilled_hotel_name ")
    Fagr_khalil=Reservation("Holyday","Fagr_Khalil","+8613094449161")
    Fagr_khalil.add_new_reservation()

#def Test_delete_a_customer():
    show.display('\t Test_delete_a_customer')
    show.display(m_b.customer_list)        
    m_a.delete_customer()           # delete customer from customer Class
    show.display(m_b.customer_list)
    
#def Test_reservation_removal():
    show.display('\t Test_reservation_removal')
    show.display(Ameer_Nezar.reservations)
    Ameer_Nezar.delete_a_reservation()   # delete customer booking from reswervation Class
    show.display(Ameer_Nezar.reservations)

#def Test_delete_a_hotel():
    show.display('\t Test_delete_a_hotel')
    show.display(Hotel.hotels)
    Rotana_hotel.delete_a_hotel() 
    show.display(Hotel.hotels)
