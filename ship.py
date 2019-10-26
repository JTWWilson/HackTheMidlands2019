# health, cannons, animal_type
class Ship:
    def __init__(self, health, cannons, animal_type):
        self.health = health
        self.cannons = cannons
        self.animal_type = animal_type

    def update_cannons(self, newCannons):
        self.cannons = newCannons
        return self.cannons

    def take_damage(self, hit_points):
        self.health -= hit_points

    def get_health(self):
        return self.health

    def destroy(self):
        print("ship destroyed")

    def get_animal_type(self):
        return self.animal_type

