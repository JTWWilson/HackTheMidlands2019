from random import normalvariate, randrange
from math import floor
from kivy.uix.widget import Widget
from kivy.core.window import Window

CANNON_SIGMA = 5

buttons_being_pressed = []


class SailingGame(Widget):

    def __init__(self, **kwargs):
        super(SailingGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')

        self._keyboard.bind(on_key_down=self._on_keyboard_down, on_key_up=self._on_keyboard_up)

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode in ['w', 'a', 's', 'd']:
            buttons_being_pressed.append(keycode)

    def _on_keyboard_up(self, keyboard, keycode, text, modifiers):
        if keycode in ['w', 'a', 's', 'd']:
            buttons_being_pressed.remove(keycode)


def take_turn(game_map, player):
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
    print(game_map)


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

        return game
