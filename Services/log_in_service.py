class Log_in_service(object):
    
    def check_id(self, id):
        if id in ["1234","4321","5678"]:
            self.id = True
        else:
            self.id = False
    
    def get_id(self):
        return self.id

    def check_pw(self, password):
        if password in ["dabbi123"]:
            self.password = True
        else:
            self.password = False

    def get_pw(self):
        return self.password