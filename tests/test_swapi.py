import unittest
import requests_mock
from src.swapi import SWAPI
from src.exceptions import FailedFetchingResource


class TestSWAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.__swapi = SWAPI("https://swapi.dev/api")

    @requests_mock.Mocker()
    def test_get_all(self, m):
        m.register_uri("GET", "https://swapi.dev/api/films",
                       [{"json": {'results': ['resp1'], "next": "https://swapi.dev/api"},
                         'status_code': 200},
                        {"json": {'results': ['resp2'], "next": None}, 'status_code': 200}])
        all_films = self.__swapi.get_all("films")
        self.assertTrue(len(all_films) == 2)

    @requests_mock.Mocker()
    def test_get_all_failure(self, m):
        m.get("https://swapi.dev/api/films", json={"bad", "data"}, status_code=500)
        with self.assertRaises(FailedFetchingResource):
            all_films = self.__swapi.get_all("films")

    @requests_mock.Mocker()
    def test_get_resources(self, m):
        m.get("https://swapi.dev/api/films/1/", json={'test': 'test'}, status_code=200)
        resources = self.__swapi.get_resources(
            ["https://swapi.dev/api/films/1/"])
        self.assertTrue(len(resources) == 1)

    @requests_mock.Mocker()
    def test_get_resources_failure(self, m):
        m.get("https://swapi.dev/api/films/1/", json={'bad': 'test'}, status_code=500)
        with self.assertRaises(FailedFetchingResource):
            resources = self.__swapi.get_resources(["https://swapi.dev/api/films/1/"])
