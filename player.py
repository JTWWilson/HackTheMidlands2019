
class Player:
    def __init__(self, playerName):
        self.player_name = playerName
        self.health = 50
        self.cannons = 1
        self.moves =[]
        self.cat_relations = None
        self.dog_relations = None
        self.map_ros = "0,0"
        self.inventory = 100

    def take_damage(self, newHealth):
        self.health -= newHealth
        return self.health

    def update_cannons(self, newCannons):
        self.cannons = newCannons
        return self.cannons

    def update_cat_rel(self, newCatRel):
        self.cat_relations = newCatRel
        return self.cat_relations

    def update_dog_rel(self, newDogRel):
        self.dog_relations = newDogRel
        return self.dog_relations

    def update_pos(self, newPos):
        self.map_pos = newPos
        return self.map_pos

    def lose_loot(self, amount_lost):
        self.inventory -= amount_lost
        return self.inventory


