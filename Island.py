import random
class Island:
    alignment = 0
    time_till_next_ship = 15

    def __init__(self):
        alignment = random.randint(1,2)
        if alignment == 1:
            alignment = 'N'
            time_till_next_ship = -1
        elif alignment == 2:
            alignment = 'C'
        elif alignment == 3:
            alignment = 'D'

    def __repr__(self):
        return Island.alignment

    def open_shop(self, player):

