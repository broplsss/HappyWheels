from UI.Header_nav import Header_nav
from Services.log_in_service import Log_in_service
import os 

class Log_in_process(Header_nav, Log_in_service):
    def __init__(self):
        # Kalla á Service klasann
        # Dæmi um það:
        # self.__video_service = VideoService()
        self.header = Header_nav()
        pass
    

    def log_in(self):
        self.id = False
        wrong_input = False
        wrong_length = False
        alpha_input = False
        while self.id == False:
            os.system('cls||clear')
            self.header.print_header_nav()
            print("\t~Log in~")
            
            ########## Villumeðhöndlun
            if wrong_input and not wrong_length and not alpha_input:
                print("Incorrect ID!")
            if wrong_length:
                print("Invalid length, ID must be 4 digits long!")
            if alpha_input and not wrong_length:
                print("ID can't contain letters!")
            ##########

            id = input("Enter your ID: ")
            print_id = id
            self.print_id = print_id #geyma original id strenginn til að prenta hann út á næstu síðu, þar sem ID: 1234 kemur

            #finna lengd af id, gera if setningu sem checkar hversu langur strengurinn er, kemur upp villumeðhöndlun
            #ef id notandi slær inn id lengra en 4 stafir
            length = Log_in_service()
            length.check_length_id(id)
            self.length = length.get_length_id()

            #checka ef alpha er í input á id
            check_alpha = Log_in_service()
            self.alpha = check_alpha.check_alpha(id)

            identity = Log_in_service()
            identity.check_id(id)
            self.id = identity.get_id() #inniheldur True eða False
            
            ######### Breytingar á gildum fyrir villumeðhöndlun
            if not self.id:
                wrong_input = True
            if not self.length:
                wrong_length = True
            else:
                wrong_length = False
            if self.alpha:
                alpha_input = False
            else:
                alpha_input = True
            ##########

    def pw_check(self):
        self.pw = False
        wrong_input = False
        wrong_length = False
        while self.pw == False:
            os.system('cls||clear')
            self.header.print_header_nav()
            print("\t~Log in~")
            print("ID:", self.print_id)

            if wrong_input and not wrong_length:
                print("Incorrect password!")
            if wrong_length:
                print("Invalid length, password must be 6 characters long!")
            
            pw = input("Enter your password: ")

            #finna lengd pw, þarf að vera 6 stafir
            length = Log_in_service()
            length.check_length_pw(pw)
            self.length = length.get_length_pw()

            password = Log_in_service()
            password.check_pw(pw)
            self.pw = password.get_pw()
            if not self.pw:
                wrong_input = True
            if not self.length:
                wrong_length = True
            else:
                wrong_length = False