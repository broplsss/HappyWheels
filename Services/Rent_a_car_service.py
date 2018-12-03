class Rent_a_car_service(object):

    def set_location(self, choice):
        if choice == "1":
            self.location = "Reykjavík"
        elif choice == "2":
            self.location = "Keflavík"
        elif choice == "3":
            self.location = "Akureyri"

    def get_location(self):
        return self.location
