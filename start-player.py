#!/usr/bin/python
# Script to choose colors for players and the starting player.

import argparse
import random

parser = argparse.ArgumentParser(description='Choose color for each player and the starting player.')
parser.add_argument('players', metavar='PLAYER', nargs='+', help='Who is playing?')
args = parser.parse_args()

remaining_colors = ["Brown", "Black", "Blue", "Green", "Gray", "Red", "Yellow"]

for player in args.players:
    color = random.choice(remaining_colors)
    remaining_colors.remove(color)
    print "%s -> %s" % (player, color)

starting_player = random.choice(args.players)
print "%s starts" % starting_player
