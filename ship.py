# health, cannons, animal_type
from math import sqrt, fabs
import random

class Ship:
    def __init__(self, health, cannons, animal_type, anger_level):
        self.health = health
        self.cannons = cannons
        self.animal_type = animal_type
        self.anger_level = anger_level
        self.map_pos = [1,1]
#
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

    def move(self, player):
        x_diff = self.map_pos[0] - player.map_pos[0]
        y_diff = self.map_pos[1] - player.map_pos[1]
        distance = sqrt((x_diff*x_diff) + (y_diff*y_diff))
        if distance <= self.anger_level:
            if fabs(x_diff) > fabs(y_diff):
                if x > 0:
                    self.map_pos[0] = self.map_pos[0] + 1
                else:
                    self.map_pos[0] = self.map_pos[0] - 1
            else:
                if y > 0:
                    self.map_pos[1] = self.map_pos[1] + 1
                else:
                    self.map_pos[1] = self.map_pos[1] - 1
        else:
            random_direction = random.randint(1, 4)
            if random_direction == 1:
                self.map_pos[0] = self.map_pos[0] + 1
            elif random_direction == 2:
                self.map_pos = self.map_pos
