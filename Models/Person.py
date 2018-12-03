class Person(object):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return "{},{},{}".format(self.name, self.phone, self.email)
    
    def __repr__(self):
        return self.__str__()

    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email