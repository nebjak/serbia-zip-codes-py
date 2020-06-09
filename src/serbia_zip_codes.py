import json
import os

db_file = open(os.path.join(os.path.dirname(__file__), 'data/db.json'))
db = json.load(db_file)


def find_by_city(city):
    pass

def find_by_zip(zip_code):
    pass

def get_all():
    pass
