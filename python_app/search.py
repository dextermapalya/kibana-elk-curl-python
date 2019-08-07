from pprint import pprint


def search(es_object, index_name, search):
    res = es_object.search(index=index_name, body=search)
    pprint(res)    