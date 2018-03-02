import pymongo


def get_matches():
    league_index = 2

    client = pymongo.MongoClient()
    db = client.xwing_ai

    collection_name = 'league_matches_{}'.format(league_index)
    collection = db[collection_name]

    doc = collection.find_one()
    return doc['matches']
