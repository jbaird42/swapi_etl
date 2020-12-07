import os
import unittest
import requests_mock
import pathlib
from tests.dummy_data import DummyData
from main import main


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        os.environ["TOP_SW_CHARACTER_LIMIT"] = "2"

    def tearDown(self) -> None:
        os.environ.pop("TOP_SW_CHARACTER_LIMIT")
        csv_filepath = f"{pathlib.Path(__file__).parent.absolute()}/star_wars_heights.csv"
        if os.path.isfile(csv_filepath):
            os.remove(csv_filepath)

    @requests_mock.Mocker()
    def test_main(self, m):
        m.register_uri("GET", "https://swapi.dev/api/films", json=DummyData.get_films())
        for i in range(4):
            character_num = i+1
            m.register_uri("GET", f"http://swapi.dev/api/people/{character_num}/",
                           json=DummyData.get_test_character(character_num))
        m.register_uri("GET", "http://swapi.dev/api/species/1/", json={"name": "human"})
        m.register_uri("POST", "https://httpbin.org/post", json={"files": {"file": "TEST SUCCESS"}})

        try:
            main()
        except Exception as e:
            self.fail(f"Test Fails. Running main() threw an exception. Exception: {e}")
