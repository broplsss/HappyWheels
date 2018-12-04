from UI.Header_nav import Header_nav
from Services.Rent_a_car_service import Rent_a_car_service
from Services.Validation import Validation
import os

class Rent_a_car_process(Header_nav, Rent_a_car_service):
    def __init__(self):
        self.__choice = Rent_a_car_service()
        self.header = Header_nav()
        self.__datetime = Validation()

    ##### PICKUP LOCATION MENU #####
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

            self.__choice.set_location(loc_choice) # Breytir choice í rétta staðsetningu
            self.location = self.__choice.get_location()   # Rétt staðsetning kominn
            if not self.location:
                wrong_input = True

    ##### CHOOSE DATE AND TIME MENU #####
    def print_pickup_menu(self):
        os.system('cls||clear')
        self.header.print_header_nav()
        print("Pick up location: {}".format(self.location))  # Location = Rvk
        print("\t~ Date and time ~")
        print("\tPage 2 of 8\n")
        ########### Implementation 
        stage = 0   # On what stage of the progress the user is on
        while stage < 4:
            if stage == 0:
                pick_up_date = input("Enter pick up date(mm/dd/yyyy): ")
                stage = self.__datetime.check_valid_date(pick_up_date, stage)
            if stage == 1:    
                pick_up_time = input("Enter pick up time(hh): ")
                stage = self.__datetime.check_valid_time(pick_up_time, stage)
            if stage == 2:
                drop_off_date = input("Enter drop off date(mm/dd/yyyy): ")
                stage = self.__datetime.check_valid_date(drop_off_date, stage)
                stage = self.__datetime.check_different_dates(pick_up_date, drop_off_date, stage)  # Checks if dates are the same or not
            if stage == 3:
                drop_off_time = input("Enter drop off time(hh): ")
                stage = self.__datetime.check_valid_time(drop_off_time, stage)
        #########################################
        date_time_list = [pick_up_date, pick_up_time, drop_off_date, drop_off_time]
        combined_loc_date_time = Rent_a_car_service()   # loc_date_time_info er location, date, og time upplýsingarnar
        self.text = combined_loc_date_time.get_combined_loc_date_time(self.location, date_time_list)

    ##### CHOOSE CAR SIZE AND BRAND MENU #####
    def print_car_size_menu(self):
        os.system('cls||clear')
        car_choice = ""
        car_size = ""   # Ónotað
        while car_choice not in ("1", "2", "3"):
            self.header.print_header_nav()
            print(self.text)
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