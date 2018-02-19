def get_lists(matches):
    lists = []
    for match in matches:
        list_1 = match['player1']['list']
        if list_1: lists.append(list_1)

        list_2 = match['player2']['list']
        if list_2: lists.append(list_2)

    return lists


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
