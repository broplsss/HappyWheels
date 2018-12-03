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

        choice = input("Choose a location: ").lower()
        # Val = Staðsetning
        
        val = Rent_a_car_service()
        val.set_location(choice)
        self.location = val.get_location()

    def print_pickup_menu(self):
        os.system('cls||clear')
        self.header.print_header_nav()
        print("Pick up location: {}".format(self.location))  # Location = Rvk
        print("\t~Date and time~")
        print("\tPage 2 of 8\n")
        pick_up_date = input("Enter pick up date(mm/dd/yy): ")