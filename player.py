
class Player:
    def __init__(self, playerName):
        self.playerName = playerName
        self.health = 50
        self.cannons = 1
        self.moves =[]
        self.catRelations = None
        self.dogRelations = None
        self.mapPos = "0,0"

    def updateHealth(self, newHealth):
        self.health = newHealth
        return self.health

    def updateCannons(self, newCannons):
        self.cannons = newCannons
        return self.cannons

    def updateCatRel(self, newCatRel):
        self.catRelations = newCatRel
        return self.catRelations

    def updateDogRel(self, newDogRel):
        self.dogRelations = newDogRel
        return self.dogRelations

    def updatePos(self, newPos):
        self.mapPos = newPos
        return self.mapPos



