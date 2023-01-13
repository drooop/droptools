from pprint import pprint
import urllib.parse

from pymongo import MongoClient

HOST = "58.210.69.90:10009/admin"
PORT = 10009
USER = "root"
PASSWORD = "iTi123456"
DATABASE = "test"


def get_data():
    username = urllib.parse.quote_plus(USER)
    password = urllib.parse.quote_plus(PASSWORD)
    uri = 'mongodb://%s:%s@%s' % (username, password, HOST)
    client = MongoClient(uri)
    db = client.get_database(DATABASE)
    return db["lab"]


if __name__ == "__main__":
    table = get_data()
    counter = 0
    for row in table.find():
        counter += 1
        pprint(row)
        if counter > 10:
            break
    
