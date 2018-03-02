import operator
from collections import defaultdict
import numpy as np


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


def get_average_pilot_count(lists):
    pilot_counts = []
    for list in lists:
        pilot_counts.append(len(list['pilots']))

    return np.average(pilot_counts)


def get_pilot_counts_histogram(lists):
    pilot_counts_histogram = defaultdict(lambda: 0)
    for list in lists:
        pilot_counts_histogram[len(list['pilots'])] += 1

    return dict(pilot_counts_histogram)


def get_average_upgrade_count(lists):
    upgrades_counts = []
    for list in lists:
        upgrades_count = 0
        for pilot in list['pilots']:
            upgrades_by_type = pilot.get('upgrades', {})
            upgrades_count += sum(len(upgrades) for upgrades in upgrades_by_type.values())
        upgrades_counts.append(upgrades_count)

    return np.average(upgrades_counts)


def get_upgrade_count_histogram(lists):
    upgrade_count_histogram = defaultdict(lambda: 0)
    for list in lists:
        upgrades_count = 0
        for pilot in list['pilots']:
            upgrades_by_type = pilot.get('upgrades', {})
            upgrades_count += sum(len(upgrades) for upgrades in upgrades_by_type.values())
        upgrade_count_histogram[upgrades_count] += 1

    return dict(upgrade_count_histogram)


def get_average_upgrade_count_per_ship(lists):
    upgrades_counts = []
    for list in lists:
        for pilot in list['pilots']:
            upgrades_by_type = pilot.get('upgrades', {})
            upgrades_count = sum(len(upgrades_by_type) for upgrades_by_type in upgrades_by_type.values())
            upgrades_counts.append(upgrades_count)

    return np.average(upgrades_counts)


def get_upgrade_count_per_ship_histogram(lists):
    upgrade_count_per_ship_histogram = defaultdict(lambda: 0)
    for list in lists:
        for pilot in list['pilots']:
            upgrades_by_type = pilot.get('upgrades', {})
            upgrades_count = sum(len(upgrades_by_type) for upgrades_by_type in upgrades_by_type.values())
            upgrade_count_per_ship_histogram[upgrades_count] += 1

    return dict(upgrade_count_per_ship_histogram)


def get_average_points(lists):
    point_costs = []
    for list in lists:
        point_costs.append(list['points'])

    return np.average(point_costs)


def get_faction_count(lists):
    factions_count = defaultdict(lambda: 0)
    for list in lists:
        factions_count[list['faction']] += 1

    return dict(factions_count)


def count_pilots_usages(lists):
    pilot_usages = defaultdict(lambda: 0)
    for list in lists:
        for pilot in list['pilots']:
            pilot_usages[pilot['name']] += 1

    return dict(pilot_usages)


def count_upgrade_usages(lists):
    upgrade_usages = defaultdict(lambda: 0)
    for list in lists:
        for pilot in list['pilots']:
            upgrades_by_type = pilot.get('upgrades', {})
            for upgrades in upgrades_by_type.values():
                for upgrade in upgrades:
                    upgrade_usages[upgrade] += 1

    return dict(upgrade_usages)
