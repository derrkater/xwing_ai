from itertools import combinations, permutations, filterfalse
from decorator import decorator


def get_cards(lists):
    """
    Creates a set of all pilot and upgrade cards used in lists from lists list.
    :param lists:
    :return:
    """
    cards = set()
    for list in lists:
        for pilot in list['pilots']:
            cards.add('{}_pilot'.format(pilot['name']))
            upgrades_by_type = pilot.get('upgrades', {})
            if upgrades_by_type:
                cards.update(set.union(*map(set, upgrades_by_type.values())))

    return cards


def shuffle_ngrams(ngrams_getter):
    def wrap_ngrams_getter(lists, n):
        ngrams = ngrams_getter(lists, n)

        permuted_ngrams = set()
        for ngram in ngrams:
            ngram = filterfalse(lambda card: not card, ngram)
            permuted_ngram = [tuple(list(x) + (n - len(x)) * ['']) for x in permutations(ngram)]
            permuted_ngrams.update(permuted_ngram)

        return permuted_ngrams

    return wrap_ngrams_getter


@shuffle_ngrams
def get_pilot_and_upgrades_ngrams(lists, n):
    """
    Creates a set of n-grams of upgrade and pilot cards of each ship in each list from lists. If ship's cards number
    is lower than n, only one n-gram, padded with '', is created.
    :param list:
    :param n:
    :return:
    """
    ngrams = set()
    for list in lists:
        ship_bags = get_ship_bags(list)
        for ship_bag in ship_bags:
            while len(ship_bag) < n: ship_bag.append('')
            ngrams.update(combinations(ship_bag, n))

    return ngrams


def get_ship_bags(list):
    """
    Creates a list of ship_bags of all ships in an input list. Ship_bag is a list of all cards of that ship,
    including pilot.
    :param list:
    :return:
    """
    ship_bags = []
    for pilot in list['pilots']:
        ship_bag = ['{}_pilot'.format(pilot['name'])]
        upgrades_by_type = pilot.get('upgrades', {})
        for upgrades in upgrades_by_type.values():
            for upgrade in upgrades:
                ship_bag.append(upgrade)

        ship_bags.append(ship_bag)

    return ship_bags
