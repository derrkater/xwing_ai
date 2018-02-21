def get_lists(matches):
    lists = []
    for match in matches:
        player_1 = match['player1']
        if player_1['list']:
            list_1 = player_1['xws']
            list_1['points'] = _get_points_from_pretty_print(player_1)
            lists.append(list_1)

        player_2 = match['player2']
        if player_2['list']:
            list_2 = player_2['xws']
            list_2['points'] = _get_points_from_pretty_print(player_2)
            lists.append(list_2)

    return lists


def _get_points_from_pretty_print(player):
    pretty_print = player['pretty_print']
    point_cost = pretty_print.split('\n')[-1][1:-1]

    return int(point_cost)


def count_lists(matches):
    lists_count = 0
    for match in matches:
        list_1 = match['player1']['list']
        if list_1: lists_count += 1

        list_2 = match['player2']['list']
        if list_2: lists_count += 1

    return lists_count


def count_pilots(lists):
    raise NotImplementedError


def count_upgrades(lists):
    raise NotImplementedError
