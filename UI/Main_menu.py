from UI.Rent_a_car_process import Rent_a_car_process

class Main_menu(object):
    def __init__(self):
        # Kalla á Service klasann
        # Dæmi um það:
        # self.__video_service = VideoService()
        pass

    def print_main_menu(self):
        print("Press 'I' for information  Press 'X' for exit")
        print("\tMain menu")
        print("\tHAPPY WHEELS")
        print("1. Continue as a Customer")
        print("2. Continue as a Salesman")
        print("3. Cancel an existing order")

        choice = input("Choose an option: ").lower()
        
        if choice == "1":
            stage = 0
            Rent_car = Rent_a_car_process()
            if stage == 0:
                Rent_car.print_location_menu()
                stage += 1
            if stage == 1:
                Rent_car.print_pickup_menu()
                stage += 1
            if stage == 2:
                Rent_car.print_car_size_menu()
                stage += 1
        elif choice == "2":
            pass


