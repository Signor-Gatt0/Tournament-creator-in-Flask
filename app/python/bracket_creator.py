from math import log2,ceil
import random
player1 = {
    "name":"a",
    "win":0,
    "lose":0
}
player2 = {
    "name":"b",
    "win":0,
    "lose":0
}
player3 = {
    "name":"c",
    "win":0,
    "lose":0
}
player4 = {
    "name":"d",
    "win":0,
    "lose":0
}
player5 = {
    "name":"e",
    "win":0,
    "lose":0
}

list_players = [player1,player2,player3,player4,player5]

def calculate_bracket_number(player_number:int) -> int:
    bracket_size:float = 2 ** ceil(log2(player_number))

    if not bracket_size % 2 == 0:
        bracket_size:int = int(bracket_size) + 1
    return bracket_size

def create_battle(list_players) -> list[tuple]:
    random.shuffle(list_players)
    
    list_of_battles = []

    bracket_size = calculate_bracket_number(player_number=len(list_players))
    ris = 0
    for i in range(bracket_size):
        if ris >= len(list_players): 
            break

        player1 = list_players[ris]
        
        if ris + 1 >= len(list_players):
            player2 = None
        else:
            player2 = list_players[ris + 1]

        ris = ris + 2
        battle = (player1,player2)
        list_of_battles.append(battle)


    return list_of_battles

def prepare_bracket(list_players:list):
    list_of_battles = create_battle(list_players)

    
