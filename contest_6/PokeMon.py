#!/usr/bin/env python3

# its helpful to manage missing keys:
from collections import defaultdict

players = defaultdict(set)
cards = defaultdict(set)

while s:= input():
  # fill in dictionaries of players and card numbers
  if s[0].isdigit():
    number, name = s.split(' / ')
    cards[number].add(name)
  else:
    player, number = s.split(' / ')
    players[player].add(number)

max_decks = []
max_total_cards = 0

for k, v in players.items():
  # try to make a deck
  deck = set()
  for elem in v:
    # deck <- union of all cards of a player
    deck = deck.union(cards[elem])

  len_deck = len(deck)
  if max_total_cards < len_deck:
    # remember longest deck
    max_total_cards = len_deck
    max_decks = [k]

  # or add another player to list, if he has same length deck
  elif max_total_cards == len_deck:
    max_decks.append(k)

for player in sorted(max_decks):
  print(player)
    
# EOF