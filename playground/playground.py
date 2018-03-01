import pymongo, operator
from utility.data_statistics import *
from utility.lists_utility import *
from objects.squadron import Squadron


def main():
    matches = get_matches()
    lists = get_lists(matches)

    print('For {} matches played there are {} lists. {} matches have both lists'.format(len(matches),
                                                                                        count_lists(matches),
                                                                                        count_matches_with_lists(
                                                                                            matches)))

    match = matches[0]
    print('MATCH: {}'.format(match))
    player_1 = match['player1']
    print('PLAYER KEYS: {}'.format(player_1.keys()))
    print('PLAYER: {}'.format(player_1))

    list = player_1['xws']
    print(len(list['pilots']))
    analyze_lists(lists)

    # print(sys.getsizeof(matches))


def get_matches():
    league_index = 2

    client = pymongo.MongoClient()
    db = client.xwing_ai

    collection_name = 'league_matches_{}'.format(league_index)
    collection = db[collection_name]

    doc = collection.find_one()
    return doc['matches']


def analyze_lists(lists):
    print('Factions:\t{}'.format(get_faction_count(lists)))
    print('Average points:\t{}'.format(get_average_points(lists)))
    print('Average pilots:\t{}'.format(get_average_pilot_count(lists)))
    print('Pilot counts histogram:\t{}'.format(get_pilot_counts_histogram(lists)))
    print('Average upgrades:\t{}'.format(get_average_upgrade_count(lists)))
    print('Upgrade count histogram:\t{}'.format(get_upgrade_count_histogram(lists)))
    print('Average upgrades/ship:\t{}'.format(get_average_upgrade_count_per_ship(lists)))
    print('Upgrade count/ship histogram:\t{}'.format(get_upgrade_count_per_ship_histogram(lists)))

    pilots_usages = count_pilots_usages(lists)
    pilots_usages_sorted = sorted(pilots_usages.items(), key=operator.itemgetter(1), reverse=True)
    print('Pilots used:\t{}'.format(len(pilots_usages)))
    print(pilots_usages_sorted)
    upgrade_usages = count_upgrade_usages(lists)
    upgrade_usages_sorted = sorted(upgrade_usages.items(), key=operator.itemgetter(1), reverse=True)
    print('Upgrades used:\t{}'.format(len(upgrade_usages)))
    print(upgrade_usages_sorted)


if __name__ == '__main__':
    main()
