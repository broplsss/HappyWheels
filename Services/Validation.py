import datetime

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

    ##### Checks if date is valid #####
    def check_valid_date(self, date, stage):
        try:    # Checkar hvort formattið sér rétt og inputtið líka
            if "/" in date:             # Ef notandi slær inn inputtið með "/" þá er það það lagað
                date = date.replace("/", "")    
            mm = date[0] + date[1]
            dd = date[2] + date[3]
            yyyy = date[4] + date[5] + date[6] + date[7]

            input_date = datetime.datetime(int(yyyy), int(mm), int(dd), 12)
            datetime_after_1year = datetime.datetime.now() + datetime.timedelta(365)    # Tíminn eftir nákvæmlega 1 ár
            if datetime.datetime.now() < input_date < datetime_after_1year: # Checkar hvort setningin passi inn í datetime format og
                stage += 1                                                           # hvort hún sé stærri en núverandi date og time
            else:      
                print("That date is invalid.")  # Annaðhvort í fortíðinni eða eftir meira en 1 ár                                                  
        except(IndexError):
            print("The format of the input date is not correct, type it in " \
            "the following format: (mm/dd/yyyy)")
        except(ValueError):
            print("The values you entered are invalid. Try entering them again.")
    
        return stage

    def check_valid_time(self, time, stage):
        try:
            datetime.time(int(time))
            stage += 1
        except(ValueError):
            print("The values you entered are invalid. Try entering them again.")
        except(TypeError):
            print("Wrong input")
    
        return stage

    def check_different_dates(self, date1, date2, stage):
        if date1 == date2:
            print("Input date's can't be the same")
            stage -= 1
    
        return stage
        ##### END #####

    def check_size_option(self,choice):
        if choice in ["a", "b", "c"]:
            return choice
        else:
            return ""

    def check_car_option(self,car_input,stage):
        if car_input in ["1","2","3","a","b","c"]:
            stage = 1
            return car_input, stage
        else:
            stage = 0
            return "", stage
        