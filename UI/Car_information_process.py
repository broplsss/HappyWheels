from UI.Header_nav import Header_nav
from Services.Car_service import Car_service
from Models.Car import Car
import os

class Car_information_process():
    def __init__(self):
        self.header = Header_nav()
        self.new_car = Car_service()
        # self.new_car_info = Car_service()

    def print_add_car_menu(self):
        os.system('cls||clear')
        self.header.print_header_nav()
        print("~ Add car ~")
        self.new_car.car_main_info_to_list()
        choice = input("Do you want to add additional info? (y/n)").lower()
        if choice == "y":
            self.new_car.car_addit_info_to_list()
        # Confirmation
        self.new_car.print_new_car_info()
        confirmation = input("Do you want to confirm this information and submit the car?: (y/n)")
        if confirmation == "y":
            self.new_car.add_car_to_repo()
        else:
            pass

    def print_car_information_menu(self):
        os.system('cls||clear')
        self.header.print_header_nav()
        print("\t~ Car Information Menu ~")
        print("1. Overview of all available cars")
        print("2. Overview of all unavailable cars")
        print("3. Find car")
        print("4. Add car\n")
        choice = input("Input choice: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            self.add_car_menu = Car_information_process()
            self.add_car_menu.print_add_car_menu()
        

    

