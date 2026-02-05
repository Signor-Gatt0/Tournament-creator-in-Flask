from math import log2,ceil
import random
player_number:int = 7 #TODO

def calculate_bracket_number(player_number:int) -> int:
    bracket_size:float = 2 ** ceil(log2(player_number))

    if not bracket_size % 2 == 0:
        bracket_size:int = int(bracket_size) + 1
    return bracket_size

def create_battle(list_players):
    # random.shuffle(list_players)
    battle = []
    list_of_battle = []

# TODO not woking as intended
    for i in range(len(list_players)):
        battle.append(list_players[i])

        if i % 2 == 0:
            list_of_battle.append(battle)
            battle = []

    print(list_of_battle)

def main(list_players:list):
    player_number:int = len(list_players)
    bracket_size = calculate_bracket_number(player_number)

lista = ["A","B","C","D","E","F","G","H","i"]
create_battle(lista)