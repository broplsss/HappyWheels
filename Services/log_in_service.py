class Log_in_service(object):
    ##########  CHECK ID
    def check_id(self, id):
        if id in ["1234","4321","5678"]:
            self.id = True
        else:
            self.id = False
    
    def get_id(self):
        return self.id
    
    ##########  CHECK PASSWORD
    def check_pw(self, password):
        if password in ["dabbi1"]:
            self.password = True
        else:
            self.password = False

    def get_pw(self):
        return self.password
    
    ##########  LENGTH ID
    def check_length_id(self, string):
        self.length = len(string)

    def get_length_id(self):
        if self.length != 4:
            return False
        else:
            return True

    ##########  ALPHA IN ID
    def check_alpha(self, id):
        try:
            for letter in id:
                int(letter)
            return True
        except ValueError:
            return False

    ##########  LENGTH PASSWORD
    def check_length_pw(self, string):
        self.length = len(string)

    def get_length_pw(self):
        if self.length != 6:
            return False
        else:
            return True