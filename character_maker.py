import sys
import random

###
# Copyright Lawrie Swinfen-Styles & Miles Bardon 2021
#
# Licensed under MIT
###

# Set values from CLI arguments or defaults
# Players in the party
players = int(sys.argv[1]) if len(sys.argv) >= 2 else 5
# Allow for repeat races
repeat_race = False if len(sys.argv) >= 3 and int(sys.argv[2]) == 0 else True
# Allow for repear classes
repeat_class = True if len(sys.argv) >= 4 and int(sys.argv[3]) == 1 else False
# Allow for customisable stats from Tasha's Cauldron of Everything
custom_stats = False if len(sys.argv) >= 5 and int(sys.argv[4]) == 0 else True
# Add RPGBOT's opinion on the combination
RPGBOT_opinion = False if len(sys.argv) >= 6 and int(
    sys.argv[5]) == 0 else True

CORE = 1  # Player's handbook, DMG, Volo's 1
MToF = 1  # Mordenkainen's Tome of Foes    2
TP = 1  # Tortle Package                 3
EEPC = 1  # Elemental Evil                 4
EGTW = 0  # Guide to Wildemount            5
GGtR = 0  # Ravnica                        6
MOoT = 0  # Theros                         7
ERLW = 0  # Eberron                        8
LR = 0  # Locathah Rising                9
AcInc = 0  # Acquisitions inc.              10
OGA = 1  # One Grung Above                11

content = [CORE, MToF, TP, EEPC, EGTW, GGtR, MOoT, ERLW, LR, AcInc, OGA]

if sum(content) == 0:
    raise ValueError("Some race content must be allowed")

races = {
    "Aarakocra":    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    "Aasimar":      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Bugbear":      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Centaur":      [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    "Changeling":   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "Dragonborn":   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Dwarf":        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Elf":          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Firbolg":      [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    "Genasi":       [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    "Gith":         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Gnome":        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Goblin":       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Goliath":      [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    "Grung":        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "Half-Elf":     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Half-Orc":     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Halfling":     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Hobgoblin":    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Hollow One":   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    "Human":        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Kalashtar":    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "Kenku":        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Kobold":       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Leonin":       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    "Lizardfolk":   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Locathah":     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    "Loxodon":      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    "Minotaur":     [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    "Orc":          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "Satyr":        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    "Shifter":      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "Simic Hybrid": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    "Tabaxi":       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Tiefling":     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Tortle":       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    "Triton":       [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    "Verdalken":    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    "Verdan":       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    "Warforged":    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "Yuan-Ti":      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}

available_races = set()

for i, source in enumerate(content):
    for race, source_list in races.items():
        if source == 1 and source_list[i] == 1:
            available_races.add(race)

available_races = list(available_races)

classes = [
    "Artificer",    # 1
    "Barbarian",   # 2
    "Bard",        # 3
    "Cleric",       # 4
    "Druid",       # 5
    "Fighter",      # 6
    "Monk",         # 7
    "Paladin",      # 8
    "Ranger",       # 9
    "Rogue",        # 10
    "Sorcerer",     # 11
    "Warlock",      # 12
    "Wizard"        # 13
]

party = []
party_numbers = []

for i in range(players):
    rn = random.randint(0, len(available_races) - 1)
    race_choice = available_races[rn]
    cn = random.randint(0, len(classes) - 1)
    class_choice = classes[cn]

    if not repeat_race and i > 1:
        if players > len(available_races):
            raise ValueError(
                'There are too many players for the number of races made available with no repeats.')
        while any(pc['race'] == race_choice for pc in party):
            rn = random.randint(0, len(available_races) - 1)
            race_choice = available_races[rn]

    if not repeat_class and i > 1:
        if players > len(classes):
            raise ValueError(
                'There are too many players for the number of classes made available with no repeats.')
        while any(pc['class'] == class_choice for pc in party):
            cn = random.randint(0, len(classes) - 1)
            class_choice = classes[cn]

    print("Player " + str(i + 1) + " should play a " +
          race_choice + " " + class_choice)
    party.append({'race': race_choice, 'class': class_choice})
    party_numbers.append({'race': rn, 'class': cn})

# Using RPGBOT's opinions on class/race synergy. Each race will be given two
# scores for each class (default rules and custom origins). Scores range
# from 1 (worst) to 4 (best). 0 means no data from RPGBOT available yet.

# Scores will be Artificer ... Wizard with customised rules, then Artificer
# ... Wizard with default rules.

synergy = [
    [3, 3, 4, 3, 4, 3, 4, 2, 3, 4, 4, 3, 3, 1, 1, 2,
        3, 4, 4, 4, 2, 4, 4, 1, 1, 1],  # 1  Aarakocra
    [3, 3, 2, 4, 3, 3, 2, 4, 3, 3, 0, 3, 2, 1, 1, 4,
        3, 1, 3, 1, 4, 1, 1, 4, 4, 1],  # 2  Aasimar
    [2, 2, 2, 2, 2, 3, 4, 3, 3, 3, 0, 3, 2, 1, 4, 1,
        2, 1, 4, 2, 2, 4, 4, 1, 1, 1],  # 3  Bugbear
    [1, 4, 2, 1, 1, 3, 1, 3, 3, 1, 0, 1, 1, 1, 4, 1,
        3, 2, 4, 1, 3, 2, 1, 1, 1, 1],  # 4  Centaur
    [1, 1, 3, 2, 2, 2, 2, 2, 2, 3, 0, 2, 2, 2, 2, 4,
        3, 2, 2, 1, 3, 2, 4, 4, 4, 1],  # 5  Changeling
    [2, 3, 3, 2, 2, 3, 3, 3, 2, 2, 0, 3, 2, 4, 4, 3,
        1, 1, 3, 1, 4, 2, 1, 4, 4, 3],  # 6  Dragonborn
    [3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 4, 4, 1,
        4, 4, 4, 2, 3, 3, 2, 1, 1, 4],  # 7  Dwarf
    [2, 2, 3, 3, 3, 3, 2, 3, 3, 4, 0, 2, 3, 4, 1,
        3, 2, 3, 4, 4, 3, 4, 4, 3, 4, 4],  # 8  Elf
    [3, 2, 3, 2, 3, 2, 2, 2, 3, 2, 0, 3, 2, 1, 2, 1,
        4, 3, 2, 2, 2, 3, 2, 1, 1, 1],  # 9  Firbolg
    [2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 0, 2, 2, 4, 4, 1,
        4, 4, 4, 2, 4, 3, 2, 1, 1, 4],  # 10 Genasi
    [2, 2, 3, 3, 3, 3, 3, 3, 2, 3, 0, 3, 4, 3, 3,
        2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 3],  # 11 Gith
    [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 0, 2, 3, 4, 1, 1,
        1, 1, 3, 2, 2, 2, 4, 3, 3, 4],  # 12 Gnome
    [2, 2, 3, 4, 3, 3, 3, 2, 3, 3, 0, 3, 3, 1, 1, 2,
        1, 1, 4, 3, 3, 4, 3, 1, 1, 1],  # 13 Goblin
    [2, 4, 3, 4, 3, 4, 3, 3, 3, 1, 0, 3, 2, 1, 4, 1,
        2, 1, 4, 1, 3, 2, 1, 1, 1, 1],  # 14 Goliath
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2,
        2, 2, 4, 4, 3, 4, 3, 1, 1, 1],  # 15 Grung
    [3, 1, 4, 3, 3, 3, 3, 3, 4, 4, 0, 3, 3, 2, 3, 4,
        3, 4, 3, 3, 4, 3, 4, 4, 4, 3],  # 16 Half-Elf
    [2, 4, 3, 3, 3, 3, 2, 3, 2, 2, 0, 3, 2, 1, 4, 2,
        1, 2, 4, 1, 3, 2, 1, 1, 1, 1],  # 17 Half-Orc
    [2, 1, 3, 2, 2, 2, 2, 2, 3, 3, 0, 2, 3, 1, 1, 4,
        4, 4, 4, 3, 4, 4, 4, 3, 4, 1],  # 18 Halfling
    [3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 1, 1,
        1, 1, 2, 1, 1, 1, 2, 1, 1, 4],  # 19 Hobgoblin
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 20 Hollow One
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # 21 Human
    [3, 3, 3, 3, 3, 2, 3, 2, 2, 2, 0, 3, 3, 1, 1, 4,
        4, 4, 1, 2, 1, 1, 2, 3, 3, 1],  # 22 Kalashtar
    [3, 2, 3, 2, 2, 2, 2, 2, 2, 3, 0, 2, 2, 1, 1, 2,
        3, 3, 3, 4, 1, 4, 3, 1, 1, 1],  # 23 Kenku
    [4, 1, 2, 2, 2, 4, 4, 3, 4, 4, 0, 4, 2, 1, 1, 2,
        1, 2, 4, 4, 4, 4, 4, 1, 1, 1],  # 24 Kobold
    [2, 3, 2, 3, 2, 3, 3, 3, 3, 2, 0, 2, 2, 1, 4, 1,
        1, 1, 4, 1, 3, 2, 1, 1, 1, 1],  # 25 Leonin
    [2, 3, 3, 2, 3, 3, 3, 2, 3, 3, 0, 2, 2, 1, 3, 1,
        4, 4, 4, 3, 2, 4, 3, 1, 2, 1],  # 26 Lizardfolk
    [2, 4, 3, 2, 3, 3, 3, 3, 3, 3, 0, 3, 3, 1, 4, 2,
        2, 2, 4, 3, 3, 3, 2, 1, 1, 1],  # 27 Locathah
    [3, 3, 3, 2, 4, 1, 2, 1, 3, 1, 0, 3, 2, 1, 2, 2,
        3, 4, 2, 2, 2, 1, 1, 1, 1, 1],  # 28 Loxodon
    [1, 4, 1, 1, 1, 4, 1, 4, 1, 1, 0, 1, 1, 1, 4, 2,
        1, 1, 4, 1, 3, 2, 1, 1, 1, 1],  # 29 Minotaur
    [3, 3, 2, 3, 2, 3, 2, 3, 3, 2, 0, 2, 1, 1, 4,
        2, 2, 1, 4, 1, 4, 2, 1, 1, 1, 1],  # 30 Orc
    [3, 3, 3, 4, 3, 4, 4, 4, 4, 4, 0, 4, 4, 1, 1, 4,
        1, 1, 2, 2, 4, 2, 3, 3, 3, 1],  # 31 Satyr
    [2, 3, 1, 2, 2, 2, 2, 2, 3, 1, 0, 2, 1, 1, 3, 2,
        2, 2, 4, 3, 4, 3, 4, 2, 2, 1],  # 32 Shifter
    [4, 4, 3, 4, 3, 4, 4, 4, 3, 3, 3, 4, 2, 4, 4, 3, 4,
        3, 3, 3, 3, 3, 3, 3, 3, 3],  # 33 Simic Hybrid
    [3, 2, 2, 3, 2, 3, 3, 3, 3, 3, 0, 2, 2, 1, 1, 4,
        1, 1, 3, 3, 4, 3, 4, 3, 3, 1],  # 34 Tabaxi
    [2, 2, 4, 2, 2, 2, 2, 3, 2, 3, 0, 3, 2, 4, 2, 4,
        2, 2, 3, 3, 4, 3, 4, 4, 4, 2],  # 35 Tiefling
    [1, 3, 3, 3, 4, 1, 2, 1, 3, 1, 0, 2, 3, 1, 4, 2,
        3, 4, 3, 2, 2, 4, 1, 1, 1, 1],  # 36 Tortle
    [3, 3, 3, 2, 2, 3, 3, 3, 3, 2, 0, 2, 2, 1, 3, 2,
        1, 1, 3, 1, 4, 2, 1, 3, 4, 1],  # 37 Triton
    [4, 2, 3, 4, 3, 3, 3, 3, 4, 4, 0, 3, 3, 4, 1, 1,
        4, 4, 1, 2, 1, 1, 1, 1, 1, 4],  # 38 Vedalken
    [2, 2, 4, 2, 2, 2, 3, 3, 2, 4, 0, 2, 3, 1, 1, 4,
        1, 1, 1, 1, 2, 1, 1, 4, 4, 1],  # 39 Verdan
    [4, 4, 3, 4, 4, 4, 3, 4, 4, 3, 0, 4, 3, 4, 4, 3,
        4, 4, 4, 3, 4, 4, 3, 3, 3, 2],  # 40 Warforged
    [4, 4, 4, 4, 3, 4, 3, 4, 4, 4, 0, 4, 4, 4, 1, 3,
        1, 1, 2, 1, 2, 1, 1, 4, 4, 4],  # 41 Yuan-Ti
]

if RPGBOT_opinion:
    for i in range(players):
        if custom_stats:
            if synergy[party_numbers[i]['race']][party_numbers[i]['class']] == 1:
                print("Player " + str(i + 1) +
                      " likely has a poor race/class combination.")
            elif synergy[party_numbers[i]['race']][party_numbers[i]['class']] == 2:
                print(
                    "Player " + str(i + 1) + " has a potentially suboptimal race/class combination.")
            elif synergy[party_numbers[i]['race']][party_numbers[i]['class']] == 3:
                print("Player " + str(i + 1) +
                      " has a good race/class combination.")
            elif synergy[party_numbers[i]['race']][party_numbers[i]['class']] == 4:
                print("Player " + str(i + 1) +
                      " has an excellent race/class combination.")
            elif synergy[party_numbers[i]['race']][party_numbers[i]['class']] == 0 and synergy[party_numbers[i]['race']][party_numbers[i]['class'] + 13] != 0:
                if synergy[party_numbers[i]['race']][party_numbers[i]['class'] + 13] == 1:
                    print(
                        "Player " + str(i + 1) + " likely has a poor race/class combination, based on default ability score data.")
                elif synergy[party_numbers[i]['race']][party_numbers[i]['class'] + 13] == 2:
                    print(
                        "Player " + str(i + 1) + " has a potentially suboptimal race/class combination, based on default ability score data.")
                elif synergy[party_numbers[i]['race']][party_numbers[i]['class'] + 13] == 3:
                    print(
                        "Player " + str(i + 1) + " has a good race/class combination, based on default ability score data.")
                elif synergy[party_numbers[i]['race']][party_numbers[i]['class'] + 13] == 4:
                    print(
                        "Player " + str(i + 1) + " has an excellent race/class combination, based on default ability score data.")
                else:
                    print("Player " + str(i + 1) +
                          " has no RPGBOT data available.")
            else:
                print("Player " + str(i + 1) + " has no RPGBOT data available.")

        else:
            if synergy[party_numbers[i]['race']][party_numbers[i]['class'] + 13] == 1:
                print("Player " + str(i + 1) +
                      " likely has a poor race/class combination.")
            elif synergy[party_numbers[i]['race']][party_numbers[i]['class'] + 13] == 2:
                print(
                    "Player " + str(i + 1) + " has a potentially suboptimal race/class combination.")
            elif synergy[party_numbers[i]['race']][party_numbers[i]['class'] + 13] == 3:
                print("Player " + str(i + 1) +
                      " has a good race/class combination.")
            elif synergy[party_numbers[i]['race']][party_numbers[i]['class'] + 13] == 4:
                print("Player " + str(i + 1) +
                      " has an excellent race/class combination.")
            else:
                print("Player " + str(i + 1) + " has no RPGBOT data available.")
