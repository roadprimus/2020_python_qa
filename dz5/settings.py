"""Модуль в ктором хранятся настройки для пакета dz5."""
from collections import namedtuple


Pair = namedtuple('Pair', ('expected', 'real'))


DOG_API_PATH = 'https://dog.ceo/dog-api/'
DOG_API_RANDOM_IMG = 'https://dog.ceo/api/breeds/image/random'
DOG_API_LIST_ALL_BREEDS = 'https://dog.ceo/api/breeds/list/all'
DOG_API_BREED_RANDOM_IMG = 'https://dog.ceo/api/breed/{name}/images/random'
DOG_API_BY_BREED = 'https://dog.ceo/api/breed/{name}/images'
DOG_API_BY_SUB_BREED = 'https://dog.ceo/api/breed/{name}/list'

OPENBREWERYD_API_PATH = 'https://www.openbrewerydb.org/'
JSONPLACEHOLDER_API_PATH = 'https://jsonplaceholder.typicode.com/'
