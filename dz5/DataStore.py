"""Здесь хранятся данные для тесов dz5."""
from random import choice

from . import settings


DOG_BREES = ('akita', 'hound', 'corgi', 'pointer')
MINUS = '-'
PLUS = ''


class Schema:
    """
    Содержит json-схемы для получаемых json-ответов от сервера.

    LIST_ALL_BREEDS - схема для фикстуры list_all_breeds из DOG API;
    MESSAGE_ARRAY - схема, когда 'message' - это список;
    MESSAGE_STRING - схема, когда 'message' - это строка.
    """

    LIST_ALL_BREEDS = {
        'type': 'object',
        'properties': {
            'message': {
                'type': 'object',
                'minProperties': 0,
                'patternProperties': {
                    '^.*$': {
                        'type': 'array',
                        'minItems': 0,
                        'items': {
                            'type': 'string'
                        }
                    }
                }
            },
            'status': {'type': 'string'}
        }
    }

    MESSAGE_ARRAY = {
        'type': 'object',
        'properties': {
            'message': {
                'type': 'array',
                'minItems': 0,
                'items': {
                    'type': 'string'
                }
            },
            'status': {'type': 'string'}
        }
    }

    MESSAGE_STRING = {
        'message': {'type': 'string'},
        'status': {'type': 'string'}
    }

    OBDB_AUTOCOMLETE = {
        'type': 'array',
        'minItems': 0,
        'items': {
            'type': 'object',
            'properties': {
                'id': {'type': 'string'},
                'name': {'type': 'string'}
            }
        }
    }

    OBDB_MAIN_ITEM = {
        'type': 'object',
        'property': {
            'brewery_type': {'type': 'string'},
            'city': {'type': 'string'},
            'country': {'type': 'string'},
            'id': {'type': 'number'},
            'latitude': {
                'type': 'string',
                'pattern': r'^-?\d+\.\d*$'
            },
            'longitude': {
                'type': 'string',
                'pattern': r'^-?\d+\.\d*$'
            },
            'name': {'type': 'string'},
            'phone': {
                'type': 'string',
                'pattern': r'^+?\d+$'
            },
            'postal_code': {
                'type': 'string',
                'pattern': r'^\d+-?\d+$'
            },
            'state': {'type': 'string'},
            'street': {'type': 'string'},
            'tag_list': {'type': 'array'},
            'updated_at': {
                'type': 'string',
                'format': 'date-time'
            },
            'website_url': {'type': 'string'}
        }
    }

    OBDB_MAIN_BREWERY = {
        'type': 'array',
        'minItems': 0,
        'items': OBDB_MAIN_ITEM
    }


store = {
    # 'test_dog_api.py'
    'api_path': [settings.DOG_API_PATH, settings.OBDB_API_PATH],
    'api_random_img': [
        {
            'schema': Schema.MESSAGE_STRING,
            'url': settings.DOG_API_RANDOM_IMG
        }
    ],
    'list_all_breeds': [
        {
            'schema': Schema.LIST_ALL_BREEDS,
            'url': settings.DOG_API_LIST_ALL_BREEDS
        }
    ],
    'by_sub_breed': [
        {
            'sub_breed': sub_breed,
            'fxt': {
                'schema': Schema.MESSAGE_ARRAY,
                'url': settings.DOG_API_BY_SUB_BREED.format(name=sub_breed)
            }
        } for sub_breed in DOG_BREES
    ],
    'by_breed': [
        {
            'breed': breed,
            'fxt': {
                'schema': Schema.MESSAGE_ARRAY,
                'url': settings.DOG_API_BY_BREED.format(name=breed)
            }
        } for breed in DOG_BREES
    ],
    'breed_random_img': [
        {
            'breed': breed,
            'fxt': {
                'schema': Schema.MESSAGE_STRING,
                'url': settings.DOG_API_BREED_RANDOM_IMG.format(name=breed)
            }
        } for breed in DOG_BREES
    ],
    # 'test_obdb.py'
    'autocomplete': [
        {
            'word': query,
            'fxt': {
                'schema': Schema.OBDB_AUTOCOMLETE,
                'url': settings.OBDB_AUTOCOMPLETE.format(query=query)
            }
        } for query in ('dog', 'cat', 'unknown', 'takogo_ne_mojet_byt')
    ],
    'per_page': [
        {
            'count': count,
            'fxt': {
                'schema': Schema.OBDB_MAIN_BREWERY,
                'url': settings.OBDB_PER_PAGE.format(count=count)
            }
        } for count in (4, 5, 10, 25, 51)
    ],
    'by_type': [
        {
            'name': name,
            'fxt': {
                'schema': Schema.OBDB_MAIN_BREWERY,
                'url': settings.OBDB_BY_TYPE.format(name=name)
            }
        } for name in ('micro', 'regional', 'brewpub')
    ],
    'get_brewery': [
        {
            'brewery_id': brewery_id,
            'fxt': {
                'schema': Schema.OBDB_MAIN_ITEM,
                'url': settings.OBDB_GET_BREWERY.format(brewery_id=brewery_id)
            }
        } for brewery_id in (123, 345, 678, 4321)
    ],
    'obdb_sort': [
        {
            'sign': sign,
            'fxt': {
                'schema': Schema.OBDB_MAIN_BREWERY,
                'url': settings.OBDB_SORT.format(sity=sity, sign=sign)
            }
        } for sity, sign in (
                ('san_diego', choice([MINUS, PLUS])),
                ('Phoenix', choice([MINUS, PLUS])),
                ('Tucson', choice([MINUS, PLUS]))
          )
    ],
}
