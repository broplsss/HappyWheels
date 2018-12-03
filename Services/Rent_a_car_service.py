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

    def get_combined_loc_date_time(self, location, pick_up_date, pick_up_time,
        drop_off_date, drop_off_time):
        loc_date_time_info = "Pick up location: {}\nPick up date: {}\n" \
        "\t Time: {}\nDrop-off date: {}\n\tTime: {}".format(location, pick_up_date,
        pick_up_time, drop_off_date, drop_off_time)
        


