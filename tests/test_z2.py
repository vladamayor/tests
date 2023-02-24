import unittest
from main import create_folder


class TestsYaDisk(unittest.TestCase):

    def test_negative(self):
        response_create, response_get = create_folder('Тест')
        self.assertEqual(response_create.status_code, 409)

    def test_positive(self):
        response_create, response_get = create_folder('Тест')
        self.assertEqual(response_create.status_code, 201)
        self.assertEqual(response_get.status_code, 200)