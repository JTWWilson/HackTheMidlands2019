import csv

class bcolors:
    MAGENTA = '\u001b[35;1m'
    YELLOW = '\u001b[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Map:
    def __repr__(self):
        with open('map.csv', 'r') as f:
            reader = csv.reader(f)
            mapBoard = list(reader)

        gameMapString = ""

        for row in mapBoard:
            for counter in range((len(row))):
                if row[counter] is "b":
                    # print("| ", "0", " |", end="")
                    gameMapString += bcolors.OKBLUE + "| " + "0" + " | " + bcolors.ENDC
                if row[counter] is "i":
                    # print("| ", "I", " |", end="")
                    gameMapString += bcolors.OKGREEN + "| " + "I" + " | " + bcolors.ENDC
                if row[counter] is "d":
                    # print("| ", "D", " |", end="")
                    gameMapString += bcolors.FAIL + "| " + "D" + " | " + bcolors.ENDC
                if row[counter] is "c":
                    # print("| ", "C", " |", end="")
                    gameMapString += bcolors.YELLOW + "| " + "C" + " | " + bcolors.ENDC
                if row[counter] is "p":
                    # print("| ", "P", " |", end="")
                    gameMapString += bcolors.BOLD + bcolors.MAGENTA + "| " + "P" + " | " + bcolors.ENDC

            gameMapString += "\n"

        return gameMapString


if __name__ == '__main__':
    gameMap = Map()
    print(gameMap)