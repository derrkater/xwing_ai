import requests
import pymongo
import logging

base_url = "http://lists.starwarsclubhouse.com/api/v1/"
leagues_url = base_url + "vassal_leagues"
league_url = base_url + "vassal_league"
matches_url = base_url + "vassal_league_matches/"

def download_and_save_league_data(league_index):

    league_json = requests.get(league_url + '/{}'.format(league_index)).json()

    client = pymongo.MongoClient()
    db = client.xwing_ai

    collection_name = 'league_{}'.format(league_index)
    collection = db[collection_name]

    collection.insert_one(league_json)

    league_id = league_json['league_name']
    league_name = league_json['name']

    return league_name, league_id

def download_and_save_league_matches(league_index):

    matches_json = requests.get(matches_url + str(league_index)).json()

    client = pymongo.MongoClient()
    db = client.xwing_ai

    collection_name = 'league_matches_{}'.format(league_index)
    collection = db[collection_name]

    collection.insert_one(matches_json)

def download_and_save_all_leagues():
    logging.basicConfig(level=logging.INFO)

    leagues_indexes = requests \
        .get(leagues_url) \
        .json()['leagues']
    logging.info('Downloading leagues: {}'.format(leagues_indexes))

    for league_index in leagues_indexes:
        league_name, league_id = download_and_save_league_data(league_index)

        download_and_save_league_matches(league_index)

        logging.info('Downloaded data from: {}({})'.format(league_name, league_id))