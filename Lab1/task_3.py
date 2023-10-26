list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

half =int(len(list_players) / 2)
half_list_1 = list_players[:half]
half_list_2 = list_players[half:]
# TODO Разделите участников на две команды
print(half_list_1, half_list_2, sep="\n")
