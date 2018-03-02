from mongo.mongo_wrapper import get_matches
from utility.lists_utility import get_lists_with_points, count_lists, count_matches_with_lists
from data_analysis.lists_statistics import analyze_lists
from utility.data_preprocessing import get_cards, get_pilot_and_upgrades_ngrams


def main():
    matches = get_matches()
    lists = get_lists_with_points(matches)

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
    print(player_1['pretty_print'])
    card_set = get_cards(lists)
    print(len(card_set), card_set)
    ngrams = get_pilot_and_upgrades_ngrams(lists, 3)
    print(ngrams)
    print(len(ngrams))


if __name__ == '__main__':
    main()
