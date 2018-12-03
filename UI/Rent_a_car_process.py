from UI.Header_nav import Header_nav
from Services.Rent_a_car_service import Rent_a_car_service
import os

class Rent_a_car_process(Header_nav, Rent_a_car_service):
    def __init__(self):
        # Kalla á Service klasann
        # Dæmi um það:
        # self.__video_service = VideoService()
        self.header = Header_nav()

    def print_location_menu(self):
        self.location = ""
        wrong_input = False
        while self.location == "":
            os.system('cls||clear')
            self.header.print_header_nav()
            print("\t~ Location ~")
            print("\tPage 1 of 8\n")
            print("Select pick up location:")
            print("1. Reykjavík")
            print("2. Keflavík")
            print("3. Akureyri")
            if wrong_input:
                print("Wrong input\tEnter a number from 1 to 3")
            loc_choice = input("Choose a location: ").lower()

            choice = Rent_a_car_service()
            choice.set_location(loc_choice) # Breytir choice í rétta staðsetningu
            self.location = choice.get_location()   # Rétt staðsetning kominn
            if not self.location:
                wrong_input = True

    def print_pickup_menu(self):
        os.system('cls||clear')
        self.header.print_header_nav()
        print("Pick up location: {}".format(self.location))  # Location = Rvk
        print("\t~ Date and time ~")
        print("\tPage 2 of 8\n")
        pick_up_date = input("Enter pick up date(mm/dd/yy): ")
        pick_up_time = input("Enter pick up time(hh): ")
        drop_off_date = input("Enter drop off date(mm/dd/yy): ")
        drop_off_time = input("Enter drop off time(hh): ")

        combined_loc_date_time = Rent_a_car_service()   # loc_date_time_info er location, date, og time upplýsingarnar
        self.text = combined_loc_date_time.get_combined_loc_date_time(self.location, pick_up_date, pick_up_time,
        drop_off_date, drop_off_time)

    def print_car_size_menu(self):
        os.system('cls||clear')
        print(self.text)
        car_choice = ""
        car_size = ""
        while car_choice not in ("1", "2", "3"):
            self.header.print_header_nav()
            print("Pick up location:",self.location)
            print("\t~ Pick a car ~")
            print("\tPage 3 of 8\n")
            print("A. Small cars (from X kr. to Y kr.") # Hér er hægt að vera búinn að vera með breytu
            if car_choice == "a":
                print("\t\tCar 1") # Get car #1 and print price
                print("\t\tCar 2") # Get car #2 and print price
                print("\t\tCar 3") # Get car #3 and print price
                
            print("B. Medium cars (from X kr. to Y kr.")    # sem eru cheapest og most expensive bílar
            if car_choice == "b":
                print("\t\tCar 1") # Get car #1 and print price
                print("\t\tCar 2") # Get car #2 and print price
                print("\t\tCar 3") # Get car #3 and print price
            print("C. SUV (from X kr. to Y kr.")
            if car_choice == "c":
                print("\t\tCar 1") # Get car #1 and print price
                print("\t\tCar 2") # Get car #2 and print price
                print("\t\tCar 3") # Get car #3 and print price
        
            car_choice = input("Choose the type of your car: ").lower()