import random
class Island:
    alignment = 0
    timeTillNextShip =  15


    def creation:
        alignment = random.randint(1,4)
        if alignment == 1:
            alignment = 'N'
        elif alignment == 2:
            alignment = 'C'
        elif alignment == 3:
            alignment = 'D'
        elif alignment == 4:
            alignment = 'A'



    def __repr__(self):
        return Island.alignment