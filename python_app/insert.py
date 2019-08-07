
def store_record(elastic_object, index_name, record):
    is_stored = True
    try:
        outcome = elastic_object.index(index=index_name, doc_type='salads', body=record)
        print(outcome)
    except Exception as ex:
        print('Error in indexing data')
        print(str(ex))
        is_stored = False
    finally:
        return is_stored
