import random
class Island:
    alignment = 0
    timeUntilNextShip = 0

    def create(self):
        alignment = random.randint(1, 4)
        timeUntilNextShip = 15

        if alignment == 1:
            #neutral
            alignment = 'N'
        elif alignment == 2:
            #cat
            alignment = 'C'
        elif alignment == 3:
            #dog
            alignment = 'D'
        elif alignment == 4:
            #allied
            alignment = 'A'

    def __repr__(self):
        return Island.alignment




