import os

def check_type_option(choice):
    if choice in ["a", "b", "c"]:
        return choice
    else:
        return ""

def check_car_option(car_input,stage):
    if car_input in ["1","2","3","a","b","c"]:
        stage = 1
        return car_input, stage
    else:
        stage = 0
        return "", stage
        
type_option = ""
car_option = ""
stage = 0
while car_option not in ["1","2","3"]:
    os.system('cls||clear')    
    print("\t~ Pick a car ~")
    print("\tPage 3 of 8\n")
    print("A. Small cars (from X kr. to Y kr.") # Hér er hægt að vera búinn að vera með breytu
    if type_option == "a":
        print("\t\tCar 1") # Get car #1 and print price
        print("\t\tCar 2") # Get car #2 and print price
        print("\t\tCar 3") # Get car #3 and print price
    
    print("B. Medium cars (from X kr. to Y kr.")    # sem eru cheapest og most expensive bílar
    if type_option == "b":
        print("\t\tCar 1") # Get car #1 and print price
        print("\t\tCar 2") # Get car #2 and print price
        print("\t\tCar 3") # Get car #3 and print price
    
    print("C. SUV (from X kr. to Y kr.")
    if type_option == "c":
        print("\t\tCar 1") # Get car #1 and print price
        print("\t\tCar 2") # Get car #2 and print price
        print("\t\tCar 3") # Get car #3 and print price

    if check_type_option(type_option) == "" and stage != 0:
        print("Invalid input")
    
    if (car_option == "" and check_type_option(type_option) != "") and stage == 0:
        print("Invalid input")

    if type_option in ["a","b","c"]:
        car_option = input("Pick a car: ").lower()
        car_option, stage = check_car_option(car_option,stage)

    if type_option not in ["a","b","c"]:
        type_option = input("Choose the type of your car: ").lower()
        stage = 1

    if car_option in ["a", "b", "c"]:
        type_option = car_option
        