"""Модуль в ктором хранятся настройки для пакета dz5."""
from collections import namedtuple


Pair = namedtuple('Pair', ('expected', 'real'))


DOG_API_PATH = 'https://dog.ceo/dog-api/'
DOG_API_RANDOM_IMG = 'https://dog.ceo/api/breeds/image/random'
DOG_API_LIST_ALL_BREEDS = 'https://dog.ceo/api/breeds/list/all'
DOG_API_BREED_RANDOM_IMG = 'https://dog.ceo/api/breed/{name}/images/random'
DOG_API_BY_BREED = 'https://dog.ceo/api/breed/{name}/images'
DOG_API_BY_SUB_BREED = 'https://dog.ceo/api/breed/{name}/list'

OBDB_API_PATH = 'https://www.openbrewerydb.org/'
OBDB_AUTOCOMPLETE = (
    'https://api.openbrewerydb.org/breweries/autocomplete?query={query}')
OBDB_PER_PAGE = 'https://api.openbrewerydb.org/breweries?per_page={count}'
OBDB_BY_TYPE = 'https://api.openbrewerydb.org/breweries?by_type={name}'
OBDB_GET_BREWERY = 'https://api.openbrewerydb.org/breweries/{brewery_id}'
OBDB_SORT = (
    'https://api.openbrewerydb.org/breweries?by_city={sity}&sort={sign}id')

JSONPLACEHOLDER_API_PATH = 'https://jsonplaceholder.typicode.com/'
