from UI.Header_nav import Header_nav
from UI.Rent_a_car_process import Rent_a_car_process
from UI.Car_information_process import Car_information_process
import os

class Salesman_menu(Header_nav):
    def __init__(self):
        self.header = Header_nav()
        self.Rent_car = Rent_a_car_process()
        self.Car_info = Car_information_process()

    def print_menu(self):
        os.system('cls||clear')
        self.header.print_header_nav()
        print("\t~Salesman Menu~")
        print("1. Rent a car")
        print("2. Search for order")
        print("3. Customer information")
        print("4. Cars information")
        print("5. Operation log")
        print("6. Change password")
        print("7. Shortcuts instruction\n")
        choice = input("Input choice: ")

        if choice == "1":
            self.Rent_car.print_location_menu()
            self.Rent_car.print_pickup_menu()
        if choice == "4":
            self.Car_info.print_car_information_menu()
            self.Car_info.print_add_car_menu()