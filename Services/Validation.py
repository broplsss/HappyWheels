from UI.Main_menu import Main_menu

class Validation(object):
    def check_input_p_h_x(self, choice):    # Navigation-ið á öllum síðum
        if choice == "p":
            # Til baka um síðu
            pass
        elif choice == "h":
            ui = Main_menu()
            ui.print_main_menu()
        elif choice == "x":
            exit()

    def check_valid_loc(self, choice):
        check_input_p_h_x(choice)
        if choice in ("1", "2", "3"):
            return True
        else:
            return False