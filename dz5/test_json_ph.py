"""Модуль для тестирования openbrewerydb.org API."""
from .BaseTestAPI import BaseTestAPI


class TestOpenBreweryDB(BaseTestAPI):
    """Тесты для API сервиса openbrewerydb.org."""

    def test_comments(self, comments):
        """
        Тест полученных данных по комментариям.

        - Делаю запрос на получение комментариев;
        - Проверяю корректность полученного ответа;

        :param comments: Фикстура для запроса получения постов.
            Словарь, содержащий:
                fxt - соловарь, содержиащий
                    url - путь для запроса,
                    schema - json-схема, ожидая в полученном ответе.
        """
        self.get_and_validate_responce(comments['fxt'])

    def test_comments_by_post_id(self, comments_by_post_id):
        """
        Тест полученных постов по идентификатору пользователя.

        - Делаю запрос на получение комментариев к выбранному посту;
        - Проверяю корректность полученного ответа;
        - Проверяю, что в полученном ответе есть только комментарии к
          выбранному посту.

        :param comments_by_post_id: Фикстура для запроса получения
             комментариев.
            Словарь, содержащий:
                post_id - идентификатор выбранного поста.
                fxt - соловарь, содержиащий
                    url - путь для запроса,
                    schema - json-схема, ожидая в полученном ответе.
        """
        r = self.get_and_validate_responce(comments_by_post_id['fxt'])
        expected_post_ids = set([comments_by_post_id['post_id']])

        real_post_ids = set([row['postId'] for row in r.json()])

        assert expected_post_ids == real_post_ids,\
            'Ожидаемый идентификатор поста не совпадает с полученным.'

    def test_posts(self, posts):
        """
        Тест полученных данных по постам.

        - Делаю запрос на получение постов;
        - Проверяю корректность полученного ответа;

        :param posts: Фикстура для запроса получения постов.
            Словарь, содержащий:
                fxt - соловарь, содержиащий
                    url - путь для запроса,
                    schema - json-схема, ожидая в полученном ответе.
        """
        self.get_and_validate_responce(posts['fxt'])

    def test_posts_by_user_id(self, posts_by_user_id):
        """
        Тест полученных постов по идентификатору пользователя.

        - Делаю запрос на получение постов выбранного пользователя;
        - Проверяю корректность полученного ответа;
        - Проверяю, что в полученном ответе есть только посты выбранного
          пользователя.

        :param comments: Фикстура для запроса получения постов.
            Словарь, содержащий:
                user_id - идентификатор выбранного пользователя.
                fxt - соловарь, содержиащий
                    url - путь для запроса,
                    schema - json-схема, ожидая в полученном ответе.
        """
        r = self.get_and_validate_responce(posts_by_user_id['fxt'])
        expected_user_ids = set([posts_by_user_id['user_id']])

        real_user_ids = set([row['userId'] for row in r.json()])

        assert expected_user_ids == real_user_ids,\
            'Ожидаемый идентификатор пользователя не совпадает с полученным.'

    def test_users(self, users):
        """
        Тест полученных данных по пользователям.

        - Делаю запрос на получение пользователей;
        - Проверяю корректность полученного ответа;

        :param userss: Фикстура для запроса получения пользователей.
            Словарь, содержащий:
                fxt - соловарь, содержиащий
                    url - путь для запроса,
                    schema - json-схема, ожидая в полученном ответе.
        """
        self.get_and_validate_responce(users['fxt'])
