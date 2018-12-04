
class Validation():
    def check_input_p_h_x(self, choice):    # Navigation-ið á öllum síðum
        if choice == "p":
            # Til baka um síðu
            pass
        elif choice == "h":
            # Fer aftur á main menu
            pass
        elif choice == "x":
            exit()

    def check_valid_loc(self, choice):
        check = Validation()
        check.check_input_p_h_x(choice)
        if choice in ("1", "2", "3"):
            return True
        else:
            return False

    def check_valid_date(self, pick_date, pick_time, drop_date, drop_time):
        pass