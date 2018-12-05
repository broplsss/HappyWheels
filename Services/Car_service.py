from Models.Car import Car
import os

class Car_service(Car):
    def __init__(self):
        self.car_info = ["Plate_number","Car","Transmission","Seats","Color","Doors","Suit_cases", \
        "Fuel_type","Year","Price","Insurance", "Kilometers", "CO2", "Highlander"]
        self.car_list = []      

    def car_main_info_to_list(self):
        for info in self.car_info[:11]:
            os.system('cls||clear')
            if info == "Transmission":
                print(info)
                print("\t1. Manual")
                print("\t2. Automatic")
                choice = input("Choose an option: ")
                if choice == "1":
                    self.car_list.append("Manual")
                elif choice == "2":
                    self.car_list.append("Automatic")
            else:
                item = input("{}: ".format(info))
                self.car_list.append(item)

    def car_addit_info_to_list(self):
        for info in self.car_info[11:]:
            os.system('cls||clear')
            item = input("{}: ".format(info))
            self.car_list.append(item)

    def print_new_car_info(self):
        for i in range(len(self.car_list)):
            print("{}: {}".format(self.car_info[i], self.car_list[i]))
