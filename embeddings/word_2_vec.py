from torch import nn
import torch.nn.functional as F

from mongo.mongo_wrapper import get_matches
from utility.lists_utility import get_lists_with_points
from utility.data_preprocessing import get_cards

EMBEDDING_DIM = 20
CONTEXT_SIZE = 3

MATCHES = get_matches()
LISTS = get_lists_with_points(MATCHES)
CARDS_SET = get_cards(LISTS)
CARDS_NUMBER = len(CARDS_SET)

card_to_index = {card: index for index, card in enumerate(CARDS_SET)}


class EmbeddingModel(nn.Module):

    def __init__(self, cards_number, embedding_dim, context_size):
        super(EmbeddingModel, self).__init__()
        self.embeddings = nn.Embedding(cards_number, embedding_dim)
        self.linear1 = nn.Linear(context_size * embedding_dim, 128)
        self.linear2 = nn.Linear(128, CARDS_NUMBER)

    def forward(self, inputs):
        embeds = self.embeddings(inputs).view((1, -1))
        out = F.relu(self.linear1(embeds))
        out = self.linear2(out)
        log_probs = F.log_softmax(out, dim=1)
        return log_probs
