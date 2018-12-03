from UI.Header_nav import Header_nav
from Services.Rent_a_car_service import Rent_a_car_service
import os

class Rent_a_car_process(Header_nav, Rent_a_car_service):
    def __init__(self):
        # Kalla á Service klasann
        # Dæmi um það:
        # self.__video_service = VideoService()
        self.header = Header_nav()
        pass

    def print_location_menu(self):
        os.system('cls||clear')
        self.header.print_header_nav()
        print("\t~Location~")
        print("\tPage 1 of 8\n")
        print("Select pick up location:")
        print("1. Reykjavík")
        print("2. Keflavík")
        print("3. Akureyri")

        num = input("Choose a location: ").lower()
        # Val = Staðsetning
        
        choice = Rent_a_car_service()
        choice.set_location(num)
        self.location = choice.get_location()

    def print_pickup_menu(self):
        os.system('cls||clear')
        self.header.print_header_nav()
        print("Pick up location: {}".format(self.location))  # Location = Rvk
        print("\t~Date and time~")
        print("\tPage 2 of 8\n")
        pick_up_date = input("Enter pick up date(mm/dd/yy): ")
        pick_up_time = input("Enter pick up time(hh): ")
        drop_off_date = input("Enter drop off date(mm/dd/yy): ")
        drop_off_time = input("Enter drop off time(hh): ")

        combined_loc_date_time = Rent_a_car_service()   # loc_date_time_info er location, date, og time upplýsingarnar
        combined_loc_date_time.get_combined_loc_date_time(self.location, pick_up_date, pick_up_time,
        drop_off_date, drop_off_time)


    def print_car_size_menu(self):
        os.system('cls||clear')
        self.header.print_header_nav()
        print("Pick up location:",self.location)