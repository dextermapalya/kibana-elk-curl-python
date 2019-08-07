import logging
from elasticsearch import Elasticsearch

def connect_elasticsearch():
    _es = None
    #_es = Elasticsearch([{'host': 'localhost', http_auth=('elastic', '4gKmFvoWMMcOPgdhj9V4'), 'port': 9200}])
    _es = Elasticsearch("http://elasticsearch:9200", http_auth=('elastic','4gKmFvoWMMcOPgdhj9V4'))
    print(_es.info())
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es

