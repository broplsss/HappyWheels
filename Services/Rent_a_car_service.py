from Services.Validation import Validation
import datetime

class Rent_a_car_service(object):

    ##### Return correct location #####
    def set_location(self, choice):
        loc_validation = Validation()   # Checks if user input P, H or X
        if loc_validation.check_valid_loc(choice):  # Er true ef choice var 1, 2 eða 3
            if choice == "1":
                self.location = "Reykjavík"
            elif choice == "2":
                self.location = "Keflavík"
            elif choice == "3":
                self.location = "Akureyri"
        else:       # Ef notandi valdi ekki 1, 2 eða 3
            print("Invalid input!")
            self.location = ""

    def get_location(self):
        return self.location
    ##### END #####

    ##### Combines date/time #####
    
    def get_combined_loc_date_time(self, location, date_time_list):
        return "Pick up location: {}\nPick up date: {}\n" \
        "\t Time: {}\nDrop-off date: {}\n\tTime: {}".format(location, date_time_list[0],
        date_time_list[1], date_time_list[2], date_time_list[3])
    ##### END #####

        


