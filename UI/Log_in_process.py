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
        while self.id == False:
            os.system('cls||clear')
            self.header.print_header_nav()
            print("\t~Log in~")
            
            if wrong_input:
                print("Invalid ID")
            id = input("Enter your ID: ")
            print_id = id
            self.print_id = print_id #geyma original id strenginn til að prenta hann út á næstu síðu, þar sem ID: 1234 kemur
            
            identity = Log_in_service()
            identity.check_id(id)
            self.id = identity.get_id() #inniheldur True eða False
            if not self.id:
                wrong_input = True

    
    def pw_check(self):
        self.pw = False
        wrong_input = False
        while self.pw == False:
            os.system('cls||clear')
            self.header.print_header_nav()
            print("\t~Log in~")
            print("ID:", self.print_id)
            
            if wrong_input:
                print("Password is incorrect")
            pw = input("Enter your password: ")
            password = Log_in_service()
            password.check_pw(pw)
            self.pw = password.get_pw()
            if not self.pw:
                wrong_input = True