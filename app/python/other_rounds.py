def who_won(list_of_battle):
    list_winners = []
    for battle in list_of_battle:
        player = battle[0]
        if player["winned"]:
            #p1 winned
            list_winners.append(battle[0])
        else:
            #p2 winned
            list_winners.append(battle[1])