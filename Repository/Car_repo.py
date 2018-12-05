from Models.Car import Car
import csv

class Car_repo(Car):
    def __init__(self):
        pass

    # Skrifa í
    def write_to_file(self, new_car_info):
        with open("./Data/Cars.csv", "a+", newline='') as cars_data:
            csv_writer = csv.writer(cars_data)
            csv_writer.writerow(new_car_info)

    # Lesa úr
    def read_car_data(self):
        with open("./Data/Cars.csv", "r") as cars_data:
            csv_reader = csv.reader(cars_data)
            next(csv_reader)
            car_info = []
            for line in csv_reader:
                car_info.append(line)
            
        return car_info
    
