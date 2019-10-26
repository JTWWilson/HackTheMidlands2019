
class Player:
    def __init__(self):
        self.health = 50
        self.cannons = 1
        self.moves =[]
        self.cat_relations = None
        self.dog_relations = None
        self.map_pos = (0, 0)
        self.inventory = 100
        self.sprite = 'game-assets/octocat.png'

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

    def move_up(self, amount):
        self.map_pos[1] += amount

    def move_down(self, amount):
        self.map_pos[1] -= amount

    def move_left(self, amount):
        self.map_pos[0] += amount

    def move_right(self, amount):
        self.map_pos[0] -= amount


