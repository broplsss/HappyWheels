from Models.Car import Car
import csv

class Car_repo(Car):
    def __init__(self):
        pass

    def get_new_car(self, Headers):
        Car_list = []
        for header in Headers:
            item = input("{}: ".format(header))
            Car_list.append(item)
        return Car_list

    def Car(self):
        Headers = ["Car","Transmission","Seats","Color","Doors","Suit_cases", \
        "Fuel_type","Year","Price","Insurance","Kilometers","CO2", \
        "Plate_number","Highlander"]
        with open("Book1.csv", "a+", newline='') as file2:
            csv_writer = csv.writer(file2)
            new_car_info = get_new_car(Headers)

            csv_writer.writerow(new_car_info)

    # Lesa úr
    def main(self):
        with open("Book1.csv", "r") as file1:
            csv_reader = csv.reader(file1)
            next(csv_reader)
            for line in csv_reader:
                print(line)
        
        Car()

main()