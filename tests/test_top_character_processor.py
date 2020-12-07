import unittest
from src.top_character_processor import TopCharacterProcessor
from src.exceptions import FailedFetchingResource, TopTenCharacterException
from tests.dummy_data import DummyData
from unittest.mock import MagicMock


class TestTopCharacterProcessor(unittest.TestCase):

    def setUp(self):
        swapi = MagicMock()
        swapi.get_all = MagicMock(return_value=DummyData.films_results())
        swapi.get_resources = MagicMock(
            side_effect=[DummyData.dummy_people_resources(), DummyData.dummy_species_resources(),
                         []])
        self.__top_character_processor = TopCharacterProcessor(swapi, top_character_limit=2)

    def test_get_top_characters_by_height(self):
        results = self.__top_character_processor.get_top_characters(sort_by="height")
        self.assertTrue(len(results) == 2)
        self.assertTrue(results[1]["name"] == "Test 3")

    def test_get_top_characters_by_appearances(self):
        results = self.__top_character_processor.get_top_characters()
        self.assertTrue(len(results) == 2)
        self.assertTrue(results[0]["name"] == "Test 3")

    def test_top_character_failed_to_get_resources(self):
        swapi = MagicMock()
        swapi.get_all = MagicMock(side_effect=FailedFetchingResource())
        top_ten_processor = TopCharacterProcessor(swapi, 1)
        with self.assertRaises(FailedFetchingResource):
            top_ten_processor.get_top_characters()

    def test_top_character_failed_to_process_data(self):
        swapi = MagicMock()
        swapi.get_all = MagicMock(return_value=[{"garbage": "garbage"}])
        top_ten_processor = TopCharacterProcessor(swapi, 1)
        with self.assertRaises(TopTenCharacterException):
            top_ten_processor.get_top_characters()
