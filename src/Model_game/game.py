from collections import Counter
from player import *

class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        for _ in range(self.matches):
            if player1.put_candies() == player2.put_candies() == False:
                res = (0, 0)
            elif player1.put_candies() == player2.put_candies() == True:
                res = (2, 2)
            elif player1.put_candies() < player2.put_candies():
                res = (3, -1)
            elif player1.put_candies() > player2.put_candies():
                res = (-1, 3)

            player1.res_raunds_appand(res[0])
            player2.res_raunds_appand(res[1])

        self.registry.update({player1.name: sum(player1.get_result_raunds())})
        self.registry.update({player2.name: sum(player2.get_result_raunds())})

        player1.del_result_raunds()
        player2.del_result_raunds()
        
    def top3(self):
        for i in self.registry.most_common(3):
            print(i[0], i[1])
