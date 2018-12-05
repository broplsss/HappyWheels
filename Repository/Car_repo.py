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
    def read_file(self):
        with open("Book1.csv", "r") as file1:
            csv_reader = csv.reader(file1)
            next(csv_reader)
            for line in csv_reader:
                print(line)
        
