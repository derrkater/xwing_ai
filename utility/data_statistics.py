from collections import defaultdict
import numpy as np


def get_average_pilot_count(lists):
    pilot_counts = []
    for list in lists:
        pilot_counts.append(len(list['pilots']))

    return np.average(pilot_counts)


def get_pilot_counts_histogram(lists):
    raise NotImplementedError


def get_average_upgrade_count(lists):
    upgrades_counts = []
    for list in lists:
        upgrades_count = 0
        for pilot in list['pilots']:
            upgrades_by_type = pilot.get('upgrades', {})
            upgrades_count += sum(len(upgrades_by_type) for upgrades_by_type in upgrades_by_type.values())
        upgrades_counts.append(upgrades_count)

    return np.average(upgrades_counts)


def get_upgrade_count_histogram(lists):
    raise NotImplementedError


def get_average_upgrade_count_per_ship(lists):
    upgrades_counts = []
    for list in lists:
        for pilot in list['pilots']:
            upgrades_by_type = pilot.get('upgrades', {})
            upgrades_count = sum(len(upgrades_by_type) for upgrades_by_type in upgrades_by_type.values())
            upgrades_counts.append(upgrades_count)

    return np.average(upgrades_counts)



def get_upgrade_count_per_ship_histogram(lists):
    raise NotImplementedError


def get_average_points(lists):
    point_costs = []
    for list in lists:
        point_costs.append(list['points'])

    return np.average(point_costs)


def get_faction_count(lists):
    factions_count = defaultdict(lambda: 0)
    for list in lists:
        factions_count[list['faction']] += 1

    return factions_count
