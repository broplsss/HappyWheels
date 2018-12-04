from UI.Header_nav import Header_nav
from Models.Car import Car
import os

class Car_information_process(Car):
    def __init__(self):
        self.header = Header_nav()

    def car_information_menu(self):
        os.system('cls||clear')
        self.header.print_header_nav()
        print("\t~ Car Information Menu ~")
        print("1. Overview of all available cars")
        print("2. Overview of all unavailable cars")
        print("3. Find car")
        print("4. Add car")

    def add_car_menu():
        os.system('cls||clear')
        self.header.print_header_nav()

