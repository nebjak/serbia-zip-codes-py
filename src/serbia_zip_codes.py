import json
import os
import re

db_file = open(os.path.join(os.path.dirname(__file__), 'data/db.json'))
db = json.load(db_file)


def find_by_city(city):
    result = []
    patern = re.compile(r'%s' % city, re.IGNORECASE)
    for item in db:
        if patern.match(item['city']):
            result.append(item)
    
    return result

def find_by_zip(zip_code):
    pass

def get_all():
    pass
