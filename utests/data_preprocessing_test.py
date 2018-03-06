from unittest import TestCase

from utility.data_preprocessing import get_ship_bags, get_pilot_and_upgrades_ngrams, shuffle_ngrams

TEST_PLAYER = {'division_name': 'planet_1', 'list': 'url_1', 'name': 'player_name',
               'pretty_print': 'pilot_1 + up_1 + up_2 + up_3\npilot_2 + up_1 + up_4\npilot_3\n(100)', 'score': 0,
               'xws': {'faction': 'rebel', 'pilots': [{'name': 'pilot_1', 'ship': 'ship_1',
                                                       'upgrades': {'crew': ['up_1'], 'ept': ['up_2'],
                                                                    'mod': ['up_3']}},
                                                      {'name': 'pilot_2', 'ship': 'ship_2',
                                                       'upgrades': {'crew': ['up_1'], 'system': ['up_4']}},
                                                      {'name': 'pilot_3', 'ship': 'ship_3'}],
                       'vendor': {'listjuggler': {}}, 'version': '4.2.0', 'points': 100}}
TEST_LIST = TEST_PLAYER['xws']


class DataPreprocessingTest(TestCase):

    def test_get_ship_bags(self):
        expected_bags = [['pilot_1', 'up_1', 'up_2', 'up_3'],
                         ['pilot_2', 'up_1', 'up_4'],
                         ['pilot_3']]
        for actual, expected in zip(get_ship_bags(TEST_LIST), expected_bags):
            self.assertTupleEqual(tuple(actual), tuple(expected))

    # def test_get_pilot_and_upgrades_ngrams(self):
    #     expected_ngrams = (('pilot_1', 'up_1'),
    #                        ('pilot_1', 'up_2'),
    #                        ('pilot_1', 'up_3'),
    #                        ('up_1', 'up_2'),
    #                        ('up_1', 'up_3'),
    #                        ('up_2', 'up_3'),
    #                        ('pilot_2', 'up_1'),
    #                        ('pilot_2', 'up_4'),
    #                        ('up_1', 'up_4'),
    #                        ('pilot_3', ''))
    #     actual_ngrams = get_pilot_and_upgrades_ngrams.__wrapped__([TEST_LIST], 2)
    #     for actual, expected in zip(sorted(actual_ngrams), sorted(expected_ngrams)):
    #         self.assertTupleEqual(actual, expected)

    #TODO: learn to mock decorators and write good unit tests in general...
