from unittest import TestCase
from main import search_russia_city, search_max_sales_volume, search_unic_uds

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

class TestsSearchRussia(TestCase):
    def test_equal(self):
        res = search_russia_city(geo_logs)
        self.assertEqual(len(res), 6)

    def test_is_(self):
        res = search_russia_city(geo_logs)
        self.assertIs(type(res), list)
        for el in res:
            self.assertIs(type(el), dict)

    def test_in_russia(self):
        res = search_russia_city(geo_logs)
        for el in res:
            self.assertIn('Россия', list(el.values())[0])


ids = {'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]}

class TestsSearchUnicUds(TestCase):
    def test_iqual(self):
        result = [213, 15, 54, 119, 98, 35]
        res = search_unic_uds(ids)
        self.assertEqual(res, result)
        self.assertEqual(len(res), 6)

    def test_is_type(self):
        res = search_unic_uds(ids)
        self.assertIs(type(res), list)


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

class TestsSearchMax(TestCase):
    def test_eq_result(self):
        res = search_max_sales_volume(stats)
        self.assertEqual(res, 'yandex')

    def test_type_res(self):
        res = search_max_sales_volume(stats)
        self.assertIs(type(res), str)
