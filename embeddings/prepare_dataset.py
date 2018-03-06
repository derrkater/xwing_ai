import csv, json
from random import shuffle

from utility.lists_utility import get_lists_with_points
from utility.data_preprocessing import get_pilot_and_upgrades_ngrams, get_cards
from mongo.mongo_wrapper import get_matches

PATH = '/Users/derrkater/PycharmProjects/xwing_ai/datasets'


def load_ngrams_dataset(n):
    with open('{}/ngrams_{}.tsv'.format(PATH, n), 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        return [(d[0], d[1:]) for d in reader]


def save_ngrams_dataset(n):
    lists = get_lists_with_points(get_matches())
    dataset = list(get_pilot_and_upgrades_ngrams(lists, n))
    shuffle(dataset)
    with open('{}/ngrams_{}.tsv'.format(PATH, n), 'w+') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(dataset)


def load_card_to_index():
    return dict(json.load(open('{}/card_to_index.json'.format(PATH), 'r')))


def save_card_to_index():
    matches = get_matches()
    lists = get_lists_with_points(matches)
    cards_set = get_cards(lists)
    cards_set.add('')

    card_to_index = {card: index for index, card in enumerate(cards_set)}
    json.dump(card_to_index, open('{}/card_to_index.json'.format(PATH), 'w+'), indent=4)


save_ngrams_dataset(4)
save_card_to_index()
