import torch, json

from itertools import combinations

from mongo.mongo_wrapper import get_matches
from utility.lists_utility import get_lists_with_points
from utility.data_preprocessing import get_cards
from embeddings.word_2_vec import EmbeddingModel

PATH = '/Users/derrkater/PycharmProjects/xwing_ai/models'

# MATCHES = get_matches()
# LISTS = get_lists_with_points(MATCHES)
# CARDS_SET = get_cards(LISTS)

MODEL = torch.load('{}/word_2_vec_embed_6_epoch_200_lr_01'.format(PATH))
CARD_TO_INDEX = dict(json.load(open('{}/card_to_index.json'.format(PATH), 'r')))

def get_vector(card):
    v = MODEL.embeddings(torch.autograd.Variable(torch.LongTensor([CARD_TO_INDEX[card]])))
    return v / v.norm()

def get_distance(card_1, card_2):
    return get_vector(card_1).dot(get_vector(card_2))

if __name__ == '__main__':
    distances = [(get_distance(card_1, card_2), card_1, card_2) for card_1, card_2 in combinations(CARD_TO_INDEX, 2) if '' not in (card_1, card_2)]
    distances = sorted(distances, key=lambda x: float(x[0].data))

    print(distances)
