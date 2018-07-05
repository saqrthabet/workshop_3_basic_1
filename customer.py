
"""
customer.py
This is the Customer class file 
"""
class Customer():
    customer_list=[]
    #def add_customer(self,hotel_booked,customer_name,customer_number):
    def __init__(self,hotel_booked,customer_name,customer_number):
        self.hotel_booked=hotel_booked
        self.name=customer_name
        self.number=customer_number
    def __repr__(self):
        return f'Customer({self.hotel_booked!r}, {self.name !r},{self.number !r})'
        
    def check_if_duplicate(self): # check whether customer is a duplicate or not
        existed= False
        for customer in Customer.customer_list:
            if customer.name == self.name and customer.number == self.number:
                existed = True
        return existed
        
    def add_customer(self):
        if not self.check_if_duplicate():
            Customer.customer_list.append(self)

    def delete_customer(self):
        for customer in Customer.customer_list:
            if customer.name == self.name and customer.number == self.number: # jump over list elements
                Customer.customer_list.remove(customer)  # delete the(list) indicates to specific instance object
                #Customer.customer_list.remove([self.name, self.number,self.hotel_booked])

"""
OLD
class Customer():
    customer_list=[]
    def __init__(self,hotel_booked,customer_name,customer_number):
        self.hotel_booked=hotel_booked
        self.name=customer_name
        self.number=customer_number
        self.customer_list.append([self.name,self.number,self.hotel_booked])
          
    def delete_customer(self):  # def delete_customer(customer_name):
         Customer.customer_list.remove([self.name, self.number,self.hotel_booked])

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
