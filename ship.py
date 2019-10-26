# health, cannons, animal_type
class ship:
	def __init__(self, health, cannons, animal_type):
		self.health = health
		self.cannons = cannons
		self.animal_type = animal_type

	def update_cannons(self, newCannons):
        self.cannons = newCannons
        return self.cannons

    def take_damage(hit_points):
    	self.health -= hit-points

    def get_health():
    	return self.health

    def destroy():
    	print("ship destroyed")

    def get_animal_type():
    	return self.animal_type

