class Car(object):
    def __init__(self, year, kilometers, transmission, color, CO2, seats, 
    plate_number, insurance, fuel_type, car_size, brand, highlander = False):
        self.year = year
        self.kilometers = kilometers
        self.transmission = transmission
        self.color = color
        self.CO2 = CO2
        self.seats = seats
        self.plate_number = plate_number
        self.insurance = insurance
        self.fuel_type = fuel_type
        self.car_size = car_size
        self.brand = brand
        self.highlander = highlander

    def __str__(self):
        pass

    def __repr__(self):
        return self.__str__()

    def get_year(self):
        return self.year

    def get_kilometers(self):
        return self.kilometers

    def get_transmission(self):
        return self.transmission
    
    def get_color(self):
        return self.color
    
    def get_CO2(self):
        return self.CO2

    def get_seats(self):
        return self.seats

    def get_plate_number(self):
        return self.plate_number

    def get_insurance(self):
        return self.insurance
    
    def get_fuel_type(self):
        return self.fuel_type

    def get_car_size(self): # Stærð bíls; small, medium, SUV(large) / Verdflokkur basicly
        return self.car_size

    def get_brand(self):    # Heiti bíls (Frekar name?)
        return self.brand

    def get_highlander(self):
        return self.highlander