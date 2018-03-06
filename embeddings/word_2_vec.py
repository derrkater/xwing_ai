import torch
from torch import nn, optim, autograd
import torch.nn.functional as F

torch.manual_seed(1)

from mongo.mongo_wrapper import get_matches
from utility.lists_utility import get_lists_with_points
from utility.data_preprocessing import get_cards, get_pilot_and_upgrades_ngrams
from embeddings.prepare_dataset import load_ngrams_dataset, load_card_to_index

PATH = '/Users/derrkater/PycharmProjects/xwing_ai/models'

EMBEDDING_DIM = 6
CONTEXT_SIZE = 3

EPOCHS = 200

CARD_TO_INDEX = load_card_to_index()
CARDS_NUMBER = len(CARD_TO_INDEX)


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


def get_card_context_vector(context, card_to_index):
    idxs = [card_to_index[card] for card in context]
    tensor = torch.LongTensor(idxs)
    return autograd.Variable(tensor)


def main():
    dataset = load_ngrams_dataset(4)[:1000]
    print(dataset)

    losses = []
    loss_function = nn.NLLLoss()
    model = EmbeddingModel(CARDS_NUMBER, EMBEDDING_DIM, CONTEXT_SIZE)
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(EPOCHS):

        print('EPOCH: {}'.format(epoch))
        total_loss = torch.FloatTensor([0])
        for target, context in dataset:
            context_variable = get_card_context_vector(context, CARD_TO_INDEX)

            model.zero_grad()

            log_probs = model(context_variable)

            loss = loss_function(log_probs, autograd.Variable(torch.LongTensor([CARD_TO_INDEX[target]])))

            loss.backward()
            optimizer.step()

            total_loss += loss.data

        print(total_loss)
        losses.append(total_loss)
    print(losses)

    torch.save(model, '{}/word_2_vec_embed_{}_epoch_{}_lr_{}'.format(PATH, EMBEDDING_DIM, EPOCHS, '001'))


if __name__ == '__main__':
    main()
