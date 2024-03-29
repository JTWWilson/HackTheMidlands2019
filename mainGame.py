from builtins import int, range

from kivy.config import Config
from kivy.core.image import Image
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.button import Button

Config.set('kivy', 'keyboard_mode', 'systemandmulti')

from random import normalvariate, randrange
from math import floor
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

from ship import Ship
from player import Player
from Island import Island
from map import Map

CANNON_SIGMA = 5

buttons_being_pressed = []
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class SailingGame(Widget):
    def __init__(self, **kwargs):
        super(SailingGame, self).__init__(**kwargs)
        player = Player()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down, on_key_up=self._on_keyboard_up)
        self.run_game()

    def _on_keyboard_down(self, keyboard, keycode, text='', modifiers=''):
        if keycode[1] in ['w', 'a', 's', 'd']:
            buttons_being_pressed.append(keycode)
            if keycode[1] == 'w':
                player.move_up(5)
            elif keycode[1] == 'a':
                player.move_left(5)
            elif keycode[1] == 's':
                player.move_down(5)
            elif keycode[1] == 'd':
                player.move_right(5)

    def _on_keyboard_up(self, keyboard, keycode, text='', modifiers=''):
        if keycode[1] in ['w', 'a', 's', 'd']:
            buttons_being_pressed.remove(keycode[1])
            print("button pushed")

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def run_game(self):
        print("run_game")
        em1 = Ship(50, 2, "cat", 1)
        em2 = Ship(50, 3, "dog", 2)
        em3 = Ship(50, 4, "cat", 3)
        em4 = Ship(50, 1, "dog", 1)
        em5 = Ship(50, 5, "cat", 0)
        em6 = Ship(50, 2, "dog", 0)
        enemies = [em1, em2, em3, em4, em5, em6]

        is1 = Island([1, 1])
        is2 = Island([2, 1])
        is3 = Island([2, 4])
        is4 = Island([5, 3])
        islands = [is1, is2, is3, is4]

        player = Player()
        gameMap = Map()

        self.game_loop(player, enemies, gameMap, islands)

    def game_loop(player, enemies, game_map, islands, game_module):
        print("game_loop")
        game_going = True
        turns = 0

        while (game_going):
            # if (has_won(game_map, player)):
            #     game_going = False
            take_turn(game_map, player)
            turns += 1
            print(turns)


def take_turn(game_map, player):
    if buttons_being_pressed:
        move = buttons_being_pressed[-1]
        player.move(move)
    if isinstance(game_map[player.x][player.y], Ship):
        if Ship.faction.relation[player] < 0:
            fight(player, game_map[player.x][player.y])
        else:
            print('you bumped into a friend, that was rude')
    elif isinstance(game_map[player.x][player.y], Island):
        island = game_map[player.x][player.y]
        if island.faction.relation[player] > 0:
            island.open_shop(player)
        elif island.faction.relation[player] == 0:
            print('island defeated')
        else:
            fight(player, island)
    # print(game_map)
    return game_map

def has_won(game_map, player):
    return all(list([island.faction.relation[player] >= 0 for island in game_map.islands]))


def fight(player, enemy):
    def get_firepower(cannons):
        base = floor(normalvariate(cannons, CANNON_SIGMA))
        return 0 if base < 0 else base

    player_firepower = get_firepower(player.cannons)
    enemy_firepower = get_firepower(enemy.cannons)
    if player_firepower > enemy_firepower:
        player.take_damage(randrange(0, 10))
        player.lose_loot(randrange(0, 10))
    else:
        player.take_damage(randrange(20, player.get_health))
        player.loot_ship(enemy)
        enemy.sink()


class GameApp(App):
    def build(self):
        game = SailingGame()
        player = Player()
        layout = GridLayout(cols=2)
        Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)

        with layout.canvas:
            # Color(1.,0,0)
            for i in range(6):
                # dont judge this - island randomisation

                if i in(0, 2, 3, 5): #every other column
                     islandPos = randrange(6)
                else:
                    islandPos = -1

                for j in range(6):
                    Rectangle(source='game-assets/basecase_water.png', pos=(int((Window.size[0]/6) * i), int((Window.size[1]/6)*j)), size =((SCREEN_WIDTH/6), int(SCREEN_HEIGHT/6)))
                    if j == islandPos:
                        #add island
                        Rectangle(source='game-assets/island-1.png',
                                  pos=(int((Window.size[0] / 6) * i), int((Window.size[1] / 6) * j)),

                                  )
                        #we should then add an island object to the array of islands

            Rectangle(source=player.sprite, pos=(int(player.map_pos[0]), int(player.map_pos[1])), size=(150,150))

        game.add_widget(layout)
        return game

if __name__ == '__main__':
    GameApp().run()