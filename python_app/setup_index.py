def create_index(es_object, index_name='test_index'):
    created = False
    # index settings
    settings = {
        "settings": {
            "number_of_shards": 2,
            "number_of_replicas": 0
        },
        "mappings": {
            "salads": {
                "dynamic": "strict",
                "properties": {
                    "title": {
                        "type": "text"
                    },
                    "submitter": {
                        "type": "text"
                    },
                    "description": {
                        "type": "text"
                    },
                    "calories": {
                        "type": "integer"
                    },
                    "ingredients": {
                        "type": "nested",
                        "properties": {
                            "step": {"type": "text"}
                        }
                    },
                    "created_at":  {
                            "type":   "date", 
                            "format": "strict_date_optional_time||epoch_millis"
                    }
                }
            }
        }
    }

    try:
        if not es_object.indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            res = es_object.indices.create(index=index_name, include_type_name = True, ignore=400, body=settings)
            print(res)
            print('Created Index')
            created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created