import json
import logging
from time import sleep
from connector import connect_elasticsearch
from insert import store_record
from setup_index import create_index
import random, string
from datetime import datetime
from search import search

def random_generator(size=15, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

def random_date_in_epoch():
    dt = str( random.randint(1,30) ) + "." + str( random.randint(1,12) ) + "." + str(random.randint(2000, 2018) ) 
    tm = str( random.randint(0,23) ) + ":" + str( random.randint(0,59) ) + ":" + str(random.randint(0, 59) )
    d = datetime.strptime(dt + " " + tm + ",76", "%d.%m.%Y %H:%M:%S,%f").strftime('%s.%f')
    d_in_ms = int(float(d)*1000)

    return d_in_ms


def run_forever():

    es = connect_elasticsearch()
    max = 15
    idx = 15
    #check if index called recipes already exists by creating one with same name    
    if create_index(es, 'recipes'):
            print('Data indexed successfully')        
    else:
        while idx < max:
            json_data = {
                    "title": "recipe " + str( random_generator(15, 'abcdefghi98765') ),
                    "submitter": "User" + str(  random.randint(1,101) ),
                    "description": "Blah Blah Blah",
                    "calories": random.randint(1,250),
                    "created_at": random_date_in_epoch(),
                    "ingredients": [{'step': '1 bunch kale, large ' 'stems discarded, ' 'leaves finely ' 'chopped'},
                                    {'step': '1/2 teaspoon salt'}, {'step': '1 tablespoon apple ' 'cider vinegar'}, {'step': '1 apple, diced'},
                                    {'step': '1/3 cup feta cheese'}, {'step': '1/4 cup currants'}, {'step': '1/4 cup toasted pine ' 'nuts'}]
                }

            out = store_record(es, 'recipes', json_data)
            idx += 1

    search_object = {'_source': ['title'], 'query': {'range': {'calories': {'gte': 120}}}}
    search(es, 'recipes', json.dumps(search_object))
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    run_forever()


