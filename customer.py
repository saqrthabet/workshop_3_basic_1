
"""
customer.py
This is the Customer class file 
"""
class Customer():
    customer_list=[]
    def __init__(self,hotel_booked,customer_name,customer_number):
        self.hotel_booked=hotel_booked
        self.name=customer_name
        self.number=customer_number
        self.customer_list.append([self.name,self.number,self.hotel_booked])
             
    def delete_customer(self):  # def delete_customer(customer_name):
         Customer.customer_list.remove([self.name, self.number,self.hotel_booked])
         

"""
ALI

class Customer():
    customers = [] # temporary list to act as database

    def __init__(self, name, phone_num):
        if name is None or type(name) is not str:
            raise ValueError('invalid argument: name')
        elif phone_num is None or type(phone_num) is not str:
            raise ValueError('invalid argument: phone_num')
        self.name = name
        self.phone_num = phone_num

        # add new customer to customers list if not already existed
        #self.add_to_list()

    def is_added_to_list(self):
        found= False
        for customer in Customer.customers:
            if customer.name == self.name and\
                customer.phone_number == self.phone_number:
                found = True
        return found

    def add_to_list(self):
        if not self.is_added_to_list():
            Customer.customers.append(self)

    def remove_from_list(self):
        for customer in Customer.customers:
            if customer.name == self.name and\
                customer.phone_number == self.phone_number:
                Customer.customers.remove(customer)

"""    
"""
Ali_ahmed.customer_name="ali_ahmed"
Ali_ahmed.customer_list=[..,"ali_ahmed"]  # last one is ali_ahmed
Ali_ahmed.delete_customer("ali_ahmed") #delete last name appended at that time, which is 
                                      # ali_ahmed
""" 
