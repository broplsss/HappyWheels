import Header_nav from Header_nav

class Rent_a_car_menu(Header_nav):
     def __init__(self):
        # Kalla á Service klasann
        # Dæmi um það:
        # self.__video_service = VideoService()
        pass

    def Print_main_menu(self):
        # If X exit
        header = Header_nav
        header.print_header_nav()
        print("\tMain menu")
        print("\tHAPPY WHEELS")
        print("Press '1' to log in as Customer")
        print("Press '2' to log in as Salesman")
        print("Press '3' to cancel an existing order")

        action = input("Choose an option: ").lower()
        if action == "1":
            Rent_a_car_menu()
        elif action == "2":
            pass