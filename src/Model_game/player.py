class Player:
    def __init__(self, name):
        self.name = name
        self._result_raunds = []                     # результаты раундов

    def res_raunds_appand(self, res):
        self._result_raunds.append(res)

    def get_result_raunds(self):
        return self._result_raunds

    def del_result_raunds(self):
        self._result_raunds = []
        if self.name == 'Grudger' or self.name == 'Detective':
            self.offended = False

    def analysis_move_apponent(self):               # анализ хода противника
        if len(self._result_raunds) > 0:
            if self._result_raunds[-1] == 2 or self._result_raunds[-1] == 3:  #  апонент положил монету
                return  True
            else:                                                               #  апонент не положил монету
                return False
        else:
            return True


class Cheater(Player):
    def __init__(self):
        super().__init__("Cheater")
        
    def put_candies(self):
        return False

class Cooperator(Player):
    def __init__(self):
        super().__init__("Cooperator")

    def put_candies(self):
        return True
    
class Copycat(Player):
    def __init__(self):
        super().__init__("Copycat")

    def put_candies (self):
        return self.analysis_move_apponent()
        
class Grudger(Player):
    def __init__(self):
        super().__init__("Grudger")
        self.offended = False

    def put_candies(self):
        if self.offended == False:
            self.offended = [True, False][self.analysis_move_apponent()]
        if self.offended:
            return False
        else:
            return True

class Detective(Player):
    def __init__(self):
        super().__init__("Detective")
        self.offended = False

    def put_candies(self):
        if self.offended == False:
            self.offended = [True, False][self.analysis_move_apponent()]
        if len(self._result_raunds) in [0, 2, 3]:
            return True
        elif len(self._result_raunds) == 1:
            return False
        else:
            if self.offended:
                return self.analysis_move_apponent()
            else:
                return False
            
class My_Player(Player):
    def __init__(self):
        super().__init__("My_Player")
        self._round_length = 0
        self.max_length = 0

    def max_round_length(self):
        if self._round_length < len(self._result_raunds):
            self._round_length = len(self._result_raunds)
        if self._round_length != 0 and len(self._result_raunds) == 0:
            self.max_length = self._round_length
            
    def put_candies (self):

        if self.max_length == 0:
            self.max_round_length()
        else:
            if len(self._result_raunds) == self.max_length:
                return False
        return self.analysis_move_apponent()