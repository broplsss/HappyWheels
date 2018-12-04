from Services.Validation import Validation

class Rent_a_car_service(object):

    def set_location(self, choice):
        loc_validation = Validation()
        if loc_validation.check_valid_loc(choice):  # Er true ef choice var 1, 2 eða 3
            if choice == "1":
                self.location = "Reykjavík"
            elif choice == "2":
                self.location = "Keflavík"
            elif choice == "3":
                self.location = "Akureyri"
        else:
            print("Invalid input!")
            self.location = ""

    def get_location(self):
        return self.location

    def get_combined_loc_date_time(self, location, date_time_list):
        return "Pick up location: {}\nPick up date: {}\n" \
        "\t Time: {}\nDrop-off date: {}\n\tTime: {}".format(location, date_time_list[0],
        date_time_list[1], date_time_list[2], date_time_list[3])

        


