"""Здесь хранятся данные для тесов dz5."""
from . import settings


DOG_BREES = ('akita', 'hound', 'corgi', 'pointer')


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


store = {
    'test_dog_api.py': {
        'api_path': [settings.DOG_API_PATH],
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
                    'url': settings.DOG_API_BY_SUB_BREED.format(
                        name=sub_breed)
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
                    'url': (
                        settings.DOG_API_BREED_RANDOM_IMG.format(name=breed))
                }
            } for breed in DOG_BREES
        ]
    }
}
