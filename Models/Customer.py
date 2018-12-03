from Person import Person

class Customer(Person):
    def __init__(self, name, phone, email, creditcard):
        Person.__init__(self, name, phone, email)
        self.creditcard = creditcard

    def __str__(self):
        return "{},{},{},{}".format(self.name, self.phone, self.email, self.creditcard)
    
    def __repr__(self):
        return self.__str__()

    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email
    
    def get_creditcard(self):
        return self.creditcard